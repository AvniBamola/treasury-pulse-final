# TreasuryPulse Starter

Hackathon scaffold: React + Vite + TypeScript frontend, FastAPI backend, Pandas/NumPy calculations, SQLite-ready architecture.

## Requirements
- Python 3.11 or 3.12
- Node.js 20 LTS+
- Git

## Start backend
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```
API docs: http://127.0.0.1:8000/docs

## Start frontend (second terminal)
```bash
cd frontend
npm install
npm run dev
```
Frontend: http://localhost:5173

## Important
- This is a starter scaffold, not a completed treasury product.
- The upload endpoint uses an in-memory store as a quick start. Replace with SQLite repository before final integration.
- Opening balances may be missing. Never label reconstructed balances as verified bank balances.
- Exclude failed transactions from settled movements.
- Do not combine currencies without a configured reporting currency and FX convention.
- Forecast intervals and financial recommendations must be clearly labelled as estimates.
