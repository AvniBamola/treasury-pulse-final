from collections import defaultdict

def daily_net_flows(rows: list[dict], entity: str | None = None, currency: str | None = None) -> list[dict]:
    totals = defaultdict(float)
    for row in rows:
        if entity and str(row.get("Entity")) != entity:
            continue
        if currency and str(row.get("Currency", "")).upper() != currency.upper():
            continue
        if str(row.get("settlement_status", "")).lower() == "failed":
            continue
        raw_date = row.get("transaction_date(Actual)")
        if not raw_date:
            continue
        amount = float(row.get("original_amount") or 0)
        direction = str(row.get("Direction", "")).lower()
        if direction in {"inflow", "in", "credit"}:
            signed = amount
        elif direction in {"outflow", "out", "debit"}:
            signed = -amount
        else:
            continue
        totals[(str(raw_date)[:10], str(row.get("Entity")), str(row.get("Currency")))] += signed
    return [{"date": d, "entity": e, "currency": c, "net_flow": round(v, 2)}
            for (d, e, c), v in sorted(totals.items())]
