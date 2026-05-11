from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from typing import Optional

# ✅ Absolute imports — NO dots
from src.schemas import ForecastResponse, WeeklyForecast, HealthResponse

app = FastAPI(
    title="Sales Forecasting API",
    description="Forecasts next N weeks of sales per state.",
    version="1.0.0"
)

# Placeholder — replace with your real model registry later
AVAILABLE_STATES = ["Maharashtra", "Delhi", "Karnataka", "Tamil Nadu"]

@app.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        models_loaded=AVAILABLE_STATES,
        total_states=len(AVAILABLE_STATES)
    )

@app.get("/states")
def list_states():
    return {
        "total": len(AVAILABLE_STATES),
        "states": sorted(AVAILABLE_STATES)
    }

@app.get("/forecast/{state}", response_model=ForecastResponse)
def get_forecast(
    state: str,
    weeks: int = Query(default=8, ge=1, le=26)
):
    if state not in AVAILABLE_STATES:
        raise HTTPException(
            status_code=404,
            detail={
                "error": f"State '{state}' not found.",
                "available_states": AVAILABLE_STATES
            }
        )

    # ── Stub forecast — replace with real model later ──
    from datetime import date, timedelta
    today = date.today()
    forecasts = [
        WeeklyForecast(
            week_start_date=str(today + timedelta(weeks=i+1)),
            forecasted_sales=round(100000 + i * 1500, 2)
        )
        for i in range(weeks)
    ]

    return ForecastResponse(
        state=state,
        model_used="stub",
        forecast_horizon_weeks=weeks,
        generated_at=datetime.utcnow().isoformat(),
        forecasts=forecasts
    )