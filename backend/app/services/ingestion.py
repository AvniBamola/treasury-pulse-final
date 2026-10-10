import pandas as pd
REQUIRED_COLUMNS = {"transaction_date(Actual)", "Entity", "Currency", "original_amount", "Direction"}

def normalize_transactions(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["transaction_date(Actual)"] = pd.to_datetime(out["transaction_date(Actual)"], errors="coerce")
    out["original_amount"] = pd.to_numeric(out["original_amount"], errors="coerce")
    out["Entity"] = out["Entity"].astype("string").str.strip()
    out["Currency"] = out["Currency"].astype("string").str.strip().str.upper()
    out["Direction"] = out["Direction"].astype("string").str.strip().str.lower()
    return out.dropna(subset=["transaction_date(Actual)", "original_amount", "Entity", "Currency", "Direction"])
