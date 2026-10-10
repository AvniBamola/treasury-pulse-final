# Initial API contract
- GET /api/health
- POST /api/upload (multipart field `file`)
- GET /api/positions?entity=...&currency=...
- GET /api/alerts/classify?position=...&threshold=...
- POST /api/scenarios/payment-delay
- POST /api/advisor

Add forecast, thresholds, reports and access-control endpoints during integration. Keep response field names stable and use Pydantic request/response models.
