import pandas as pd

def load_data(filepath):
    """Load dataset from CSV file"""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Preprocess dataset: encode categorical features"""
    df = pd.get_dummies(df, columns=['Soil_Type'], drop_first=True)
    return df
