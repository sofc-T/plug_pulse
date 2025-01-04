from flask import Blueprint, request, jsonify
from app.utils.validation import validate_input
from models.loader import ModelLoader
import tensorflow as tf

bp = Blueprint("inference", __name__, url_prefix="/inference")

# Initialize the model loader
model_loader = ModelLoader()

@bp.route("/<model_name>", methods=["POST"])
def infer(model_name):
    """
    Handles inference requests for a specific model.
    """
    try:
        # Parse input data
        data = request.get_json()
        if not data or "instances" not in data:
            return jsonify({"error": "Invalid input data. Expected 'instances'."}), 400
        
        # Load the model
        model = model_loader.get_model(model_name)
        
        # Validate input
        instances = validate_input(data["instances"])
        
        # Perform inference
        serving_function = model.signatures["serving_default"]
        predictions = serving_function(tf.convert_to_tensor(instances))
        
        # Format predictions (assuming a key like 'output_0' exists in the output)
        result = {key: value.numpy().tolist() for key, value in predictions.items()}
        
        return jsonify({"predictions": result}), 200

    except FileNotFoundError:
        return jsonify({"error": f"Model '{model_name}' not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
