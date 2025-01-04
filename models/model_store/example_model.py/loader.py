import os
import tensorflow as tf

class ModelLoader:
    def __init__(self, model_store_path="models/model_store"):
        self.model_store_path = model_store_path
        self.models = {}

    def load_model(self, model_name):
        """
        Loads a TensorFlow model from the model_store directory.
        """
        model_path = os.path.join(self.model_store_path, model_name)
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model {model_name} not found in {self.model_store_path}.")
        
        model = tf.saved_model.load(model_path)
        self.models[model_name] = model
        return model

    def get_model(self, model_name):
        """
        Retrieves a loaded model from memory or loads it if not already loaded.
        """
        if model_name not in self.models:
            return self.load_model(model_name)
        return self.models[model_name]
