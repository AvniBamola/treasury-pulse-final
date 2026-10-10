from datetime import date, timedelta
from typing import Any


def simulate_payment_delay(
    amount: float,
    original_day: int,
    delay_days: int,
    horizon_days: int = 30,
) -> dict[str, Any]:
    """
    Simulate an incoming payment being delayed.

    Day 0 means the first day of the forecast window.
    This function changes payment timing, not the payment amount.
    """

    if amount <= 0:
        raise ValueError("Payment amount must be greater than zero.")

    if not 0 <= original_day < horizon_days:
        raise ValueError(
            "Original payment day must be inside the forecast window."
        )

    if not 1 <= delay_days <= 30:
        raise ValueError("Delay must be between 1 and 30 days.")

    if horizon_days < 1:
        raise ValueError("Forecast horizon must be at least one day.")

    new_day = original_day + delay_days

    
    payment_within_horizon = new_day < horizon_days

    return {
        "scenario": "payment_delay",
        "amount": round(amount, 2),
        "original_day": original_day,
        "delay_days": delay_days,
        "new_day": new_day if payment_within_horizon else None,
        "payment_within_horizon": payment_within_horizon,
        "interpretation": (
            "The payment arrives later; its amount is unchanged."
        ),
    }
def simulate_cash_balance(
    forecast_rows: list[dict[str, Any]],
    payment_date: str,
    payment_amount: float,
    delay_days: int,
) -> dict[str, Any]:
    """Compare daily forecast balances with a delayed-payment scenario."""

    if not forecast_rows:
        raise ValueError("Forecast data cannot be empty.")

    if payment_amount <= 0:
        raise ValueError("Payment amount must be greater than zero.")

    if not 0 <= delay_days <= 30:
        raise ValueError("Delay must be between 0 and 30 days.")

    original_date = date.fromisoformat(payment_date)
    new_payment_date = original_date + timedelta(days=delay_days)

    rows = sorted(
        forecast_rows,
        key=lambda row: date.fromisoformat(
            str(row["forecast_date"])[:10]
        ),
    )

    entity_id = rows[0]["entity_id"]
    currency = str(rows[0]["currency"]).upper()
    daily_balances = []
    forecast_dates = set()

    for row in rows:
        forecast_date = date.fromisoformat(
            str(row["forecast_date"])[:10]
        )

        if row["entity_id"] != entity_id:
            raise ValueError("Use forecast rows for one entity.")

        if str(row["currency"]).upper() != currency:
            raise ValueError("Use forecast rows for one currency.")

        if forecast_date in forecast_dates:
            raise ValueError("Duplicate forecast dates found.")

        forecast_dates.add(forecast_date)

        baseline = float(row["predicted_balance"])

        # Assumes the original forecast already includes this payment.
        payment_delayed = (
            delay_days > 0
            and original_date <= forecast_date < new_payment_date
        )

        adjustment = payment_amount if payment_delayed else 0.0
        scenario_balance = baseline - adjustment

        daily_result = {
            "forecast_date": forecast_date.isoformat(),
            "entity_id": entity_id,
            "currency": currency,
            "baseline_balance": round(baseline, 2),
            "scenario_balance": round(scenario_balance, 2),
            "difference": round(scenario_balance - baseline, 2),
        }

        for bound in ("lower_bound", "upper_bound"):
            if row.get(bound) is not None:
                daily_result[f"scenario_{bound}"] = round(
                    float(row[bound]) - adjustment, 2
                )

        daily_balances.append(daily_result)

    if original_date not in forecast_dates:
        raise ValueError("Payment date must exist in the forecast.")

    return {
        "scenario": "payment_delay",
        "entity_id": entity_id,
        "currency": currency,
        "payment_date": original_date.isoformat(),
        "new_payment_date": new_payment_date.isoformat(),
        "payment_amount": round(payment_amount, 2),
        "delay_days": delay_days,
        "payment_within_horizon": new_payment_date in forecast_dates,
        "daily_balances": daily_balances,
    }
