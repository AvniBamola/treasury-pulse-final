from fastapi import APIRouter, HTTPException
from backend.app.api.upload import TRANSACTIONS
from backend.app.services.cashflow import daily_net_flows
router = APIRouter(tags=["positions"])

@router.get("/positions")
def positions(entity: str | None = None, currency: str | None = None):
    if not TRANSACTIONS:
        raise HTTPException(status_code=409, detail="Upload a CSV first.")
    items = daily_net_flows(TRANSACTIONS, entity=entity, currency=currency)
    return {"count": len(items), "items": items}
