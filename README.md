# End-to-End Time Series Forecasting System

A production-ready sales forecasting system that trains multiple ML models,
automatically selects the best one per state, and serves predictions via a REST API.

## Problem Statement
Forecast next 8 weeks of weekly sales for each US state using historical
beverage sales data (2019–2021).

## Models Implemented
| Model | Type |
|-------|------|
| SARIMA | Statistical |
| Facebook Prophet | Time Series |
| XGBoost | Machine Learning |
| LSTM | Deep Learning |

The system automatically selects the best model per state based on RMSE
on a held-out validation set (last 8 weeks of data).

## Project Structure

forecasting-system/
├── data/
│   ├── sales_data_clean.xlsx       # Cleaned data extracted from PDF
│   └── sales_data_featured.xlsx    # Data with engineered features
├── notebooks/
│   └── .ipynb                      # EDA + Feature Engineering notebook
├── src/
│   └── api.py                      # FastAPI REST API
├── best_models.pkl                 # Saved best models per state
├── requirements.txt                # Python dependencies
└── README.md

## Feature Engineering
- Lag features: t-1, t-7, t-30 weeks
- Rolling mean and std: 4-week and 12-week windows
- Calendar features: day of week, month, week number, quarter
- Holiday flag: US public holidays
- Train/validation split: last 8 weeks held out (no data leakage)

## API Usage

### Start the server
```bash
uvicorn src.api:app --reload
```

### Endpoints

#### Get 8-week forecast for a state

Example:
```bash
curl http://localhost:8000/predict/California
```
Response:
```json
{
  "state": "California",
  "model_used": "prophet",
  "forecast": [442000000, 445000000, 448000000, 451000000,
               453000000, 456000000, 459000000, 462000000],
  "rmse": 12500000
}
```

#### List all available states

#### API documentation (auto-generated)

## Installation

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/forecasting-system.git
cd forecasting-system

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Start the API
uvicorn src.api:app --reload
```

## Requirements
- Python 3.10+
- See requirements.txt for full list

## Results
Models were evaluated on last 8 weeks of data per state.
Best model was automatically selected based on lowest RMSE.

