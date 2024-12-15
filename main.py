# main.py
from src.data_ingestion import load_data
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.model_evaluation import evaluate_model
from src.model_deployment import deploy_model
from src.utils import setup_logging
import joblib

def main():
    # Setup logging
    logger = setup_logging(level='INFO')
    
    # Load data
    train_data, test_data = load_data()
    
    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(train_data, test_data)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    evaluate_model(model, X_test, y_test)
    
    # Deploy model
    deploy_model()

if __name__ == "__main__":
    main()
