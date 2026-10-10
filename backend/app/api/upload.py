from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
from backend.app.services.ingestion import normalize_transactions, REQUIRED_COLUMNS

router = APIRouter(tags=["ingestion"])
# Quick-start in-memory store. Replace with SQLite repository for final integration.
TRANSACTIONS: list[dict] = []

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    global TRANSACTIONS
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a CSV file.")
    try:
        df = pd.read_csv(BytesIO(await file.read()))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Could not parse CSV: {exc}")
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        raise HTTPException(status_code=422, detail={
            "message": "Required columns missing", "missing_columns": missing,
            "available_columns": list(df.columns)
        })
    clean = normalize_transactions(df)
    TRANSACTIONS = clean.to_dict(orient="records")
    return {"filename": file.filename, "rows_received": len(df),
            "rows_accepted": len(clean), "rows_rejected": len(df)-len(clean),
            "message": "Loaded into in-memory starter store"}
