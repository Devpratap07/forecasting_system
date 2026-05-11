from pydantic import BaseModel
from typing import List, Optional

class WeeklyForecast(BaseModel):
    week_start_date: str
    forecasted_sales: float
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None

class ForecastResponse(BaseModel):
    state: str
    model_used: str
    forecast_horizon_weeks: int
    generated_at: str
    forecasts: List[WeeklyForecast]

class HealthResponse(BaseModel):
    status: str
    models_loaded: List[str]
    total_states: int

class ErrorResponse(BaseModel):
    error: str
    available_states: List[str]