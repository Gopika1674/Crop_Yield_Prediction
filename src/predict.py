import joblib
import pandas as pd

def load_model(model_path):
    return joblib.load(model_path)

def predict_yield(model, input_data):
    """input_data should be a dict with features"""
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]
