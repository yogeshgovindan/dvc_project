# src/model_deployment.py
import joblib
import os

def deploy_model(model_path='model/rf_model.pkl'):
    if not os.path.exists(model_path):
        print("Model path does not exist. Please train the model first.")
        return None
    
    # Load the model
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}")
    
    # This is where you can integrate deployment logic, for example, an API call or cloud service.
    return model
