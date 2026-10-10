from fastapi import APIRouter
from backend.app.services.alerts import classify_gap
router = APIRouter(tags=["alerts"])

@router.get("/alerts/classify")
def classify(position: float, threshold: float):
    return classify_gap(position, threshold)
