import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import yaml
import mlflow
import os

# Load model hyperparameters from params.yaml
def load_params():
    with open("params.yaml") as f:
        return yaml.safe_load(f)

# Training function
def train(data_path, model_path):
    df = pd.read_csv(data_path)

    # Drop non-numeric or unneeded columns
    X = df.drop(columns=["Loan_ID", "Loan_Status"], errors='ignore')
    y = df["Loan_Status"]

    # Encode categorical features in X
    le = LabelEncoder()
    for col in X.columns:
        if X[col].dtype == 'object':
            X[col] = le.fit_transform(X[col].astype(str))

    # Encode target column y if it's text
    if y.dtype == 'object':
        y = le.fit_transform(y.astype(str))

    # Load hyperparameters
    params = load_params()["train"]

    # Train the model
    model = RandomForestClassifier(
        n_estimators=params["n_estimators"],
        max_depth=params["max_depth"]
    )
    model.fit(X, y)

    # Save the model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

    # Log parameters to MLflow
    mlflow.set_experiment("Loan_Pipeline")
    with mlflow.start_run():
        mlflow.log_params(params)

# Run the training
if __name__ == "__main__":
    train("data/processed/clean_loan.csv", "models/model.pkl")

