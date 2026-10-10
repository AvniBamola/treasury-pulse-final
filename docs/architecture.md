# Architecture
React/Vite frontend -> FastAPI REST API -> shared services -> SQLite repository.

All features should reuse the same cash-position, forecast and alert services. Scenario calculations must not mutate baseline data. The assistant must retrieve calculated values rather than invent figures. Currency conversion requires a configured reporting currency and documented FX convention.
