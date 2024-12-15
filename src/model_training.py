# src/model_training.py
import os
import joblib
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train, model_type="RandomForest", n_estimators=100, max_depth=10):
    if model_type == "RandomForest":
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    
    model.fit(X_train, y_train)
    
    # Create the 'model' directory if it doesn't exist
    model_dir = 'model'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    # Save the model
    model_path = os.path.join(model_dir, 'rf_model.pkl')
    joblib.dump(model, model_path)
    print(f"Model trained and saved at {model_path}")
    return model
