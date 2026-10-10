from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.health import router as health_router
from backend.app.api.upload import router as upload_router
from backend.app.api.positions import router as positions_router
from backend.app.api.alerts import router as alerts_router
from backend.app.api.scenarios import router as scenarios_router
from backend.app.api.advisor import router as advisor_router

app = FastAPI(title="TreasuryPulse API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)
for router in [health_router, upload_router, positions_router, alerts_router, scenarios_router, advisor_router]:
    app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"name": "TreasuryPulse", "status": "running", "docs": "/docs"}
