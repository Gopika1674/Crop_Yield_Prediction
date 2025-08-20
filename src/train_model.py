import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
from preprocess import load_data, preprocess_data

def train_and_save_model(data_path, model_path):
    # Load dataset
    df = load_data(data_path)
    df = preprocess_data(df)

    # Split into features and target
    X = df.drop("Crop_Yield", axis=1)
    y = df["Crop_Yield"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Model Performance:")
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)
    print("R² Score:", r2_score(y_test, y_pred))

    # Save model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model("data/crop_data.csv", "models/random_forest.pkl")
