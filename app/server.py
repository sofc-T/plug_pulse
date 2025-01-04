from flask import Flask
from app.routes import health, metadata, inference

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(health.bp)
    app.register_blueprint(metadata.bp)
    app.register_blueprint(inference.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

