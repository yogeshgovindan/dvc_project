# src/data_ingestion.py
import pandas as pd
import yaml

def load_data(config_file='config/config.yaml'):
    # Load configuration
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    
    train_data_path = config['data']['train_data_path']
    test_data_path = config['data']['test_data_path']

    # Load data
    train_data = pd.read_csv(train_data_path)
    test_data = pd.read_csv(test_data_path)

    print(f"Data loaded: {train_data.shape[0]} train samples, {test_data.shape[0]} test samples.")
    return train_data, test_data
