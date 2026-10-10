from fastapi import APIRouter
from pydantic import BaseModel, Field
router = APIRouter(tags=["scenarios"])

class PaymentDelayRequest(BaseModel):
    amount: float = Field(gt=0)
    original_day: int = Field(ge=0, le=29)
    delay_days: int = Field(ge=1, le=5)

@router.post("/scenarios/payment-delay")
def payment_delay(req: PaymentDelayRequest):
    return {"scenario": "payment_delay", "amount": req.amount,
            "original_day": req.original_day,
            "new_day": min(29, req.original_day + req.delay_days),
            "interpretation": "Timing shifts; this is not a permanent saving."}
