from fastapi import APIRouter
from pydantic import BaseModel, Field
router = APIRouter(tags=["advisor"])

class AdvisorQuestion(BaseModel):
    question: str = Field(min_length=1, max_length=1000)

@router.post("/advisor")
def advisor(req: AdvisorQuestion):
    return {"answer": "Local fallback only. Connect this endpoint to calculated positions, forecasts and alerts before relying on it.",
            "question": req.question, "sources": [], "mode": "local_fallback"}
