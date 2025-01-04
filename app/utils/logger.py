import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PlugServe")

# --- app/utils/config.py ---
import os

MODEL_PATH = os.getenv("MODEL_PATH", "models/model_store/example_model")

# --- models/loader.py ---
import tensorflow as tf
from app.utils.logger import logger

def load_model(path):
    try:
        model = tf.saved_model.load(path)
        logger.info(f"Model loaded successfully from {path}")
        return model
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise