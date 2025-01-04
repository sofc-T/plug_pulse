Plug Serve: Endpoint Overview and File Locations
Plug Serve is a framework for deploying TensorFlow models via RESTful APIs. 
Below is a quick guide to the key endpoints and related file locations.

Plug Serve: Endpoint Overview and File Locations
Plug Serve is a framework for deploying TensorFlow models via RESTful APIs. Below is a quick guide to the key endpoints and related file locations.

Endpoints
Health Check

URL: /health
Method: GET
Purpose: Confirms that the API server is running.
Response: {"status": "healthy"}
Model Metadata

URL: /metadata/<model_name>
Method: GET
Purpose: Retrieves metadata (e.g., input/output details) about the specified model.
Response:
json
Copy code
{
    "model_name": "example_model",
    "input_signature": ["float32[5]"],
    "output_signature": ["float32[1]"]
}
Inference

URL: /inference/<model_name>
Method: POST
Purpose: Performs predictions using the specified model.
Request Body:
json
Copy code
{
    "instances": [[1.0, 2.0, 3.0, 4.0, 5.0]]
}
Response:
json
Copy code
{
    "predictions": {
        "output_0": [[0.97]]
    }
}
File Locations
Endpoint Definitions

Located in app/routes/:
health.py: Defines the health check endpoint.
metadata.py: Implements the model metadata endpoint.
inference.py: Handles model inference requests.
Model Loading

models/loader.py: Handles model storage, loading, and caching.
Model Storage

models/model_store/: Directory to store TensorFlow SavedModel files.
Utility Functions

app/utils/: Contains helper functions for validation and configuration.

pip install tensorflow
pip install flask

