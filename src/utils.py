# src/utils.py
import logging
import yaml

def setup_logging(level='INFO'):
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    return logger

def load_config(config_file='config/config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config
