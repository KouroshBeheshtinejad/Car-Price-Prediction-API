from pathlib import Path

import joblib
import numpy as np
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parent.parent / 'models' / 'car_price_pipeline.pkl'
pipe = joblib.load(MODEL_PATH)


def predict_price(input_data: dict) -> float:
    df = pd.DataFrame([input_data])

    rename_dict = {
        'Engine_HP': 'Engine HP',
        'Engine_Cylinders': 'Engine Cylinders',
        'Number_of_Doors': 'Number of Doors',
        'Transmission_Type': 'Transmission Type',
        'Engine_Fuel_Type': 'Engine Fuel Type',
        'Vehicle_Size': 'Vehicle Size',
        'Vehicle_Style': 'Vehicle Style',
    }
    df.rename(columns=rename_dict, inplace=True)

    for col in ['Engine Fuel Type', 'Vehicle Size', 'Vehicle Style', 'Driven_Wheels', 'Make']:
        if col not in df.columns or df[col].isnull().any():
            df[col] = 'unknown'

    for col in ['Engine HP', 'Engine Cylinders', 'Number of Doors', 'avg_mpg', 'Year']:
        if col not in df.columns or df[col].isnull().any():
            df[col] = 0

    y_pred_log = pipe.predict(df)
    y_pred_log = np.clip(y_pred_log, a_min=None, a_max=15)
    y_pred_real = np.expm1(y_pred_log)
    return float(y_pred_real[0])
