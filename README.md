# Car Price Prediction Web Application (Django)

This project is now a **full Django web application** for car price prediction using a trained machine learning pipeline (`models/car_price_pipeline.pkl`).

## What is included

- **Django web UI** at `/` with a complete prediction form.
- **Django JSON API** at `/api/predict/` for programmatic access.
- Existing model inference logic reused for consistent predictions.

## Project Structure

```bash
├─ carprice_site/                # Django project settings and URL config
├─ predictor/                    # Django app (forms, views, inference service, templates)
│  └─ templates/predictor/home.html
├─ models/car_price_pipeline.pkl # Trained ML pipeline
├─ manage.py                     # Django entrypoint
├─ requirements.txt
└─ app/                          # Existing FastAPI code (kept for reference)
```

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Open:
- Web app: `http://127.0.0.1:8000/`
- API endpoint: `http://127.0.0.1:8000/api/predict/`

## API usage example

```bash
curl -X POST http://127.0.0.1:8000/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{
    "Make": "Toyota",
    "Year": 2020,
    "Engine_HP": 200,
    "Engine_Cylinders": 4,
    "Transmission_Type": "Automatic",
    "Driven_Wheels": "front",
    "Vehicle_Size": "Midsize",
    "Vehicle_Style": "Sedan",
    "Number_of_Doors": 4,
    "avg_mpg": 28
  }'
```
