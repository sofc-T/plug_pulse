from flask import Blueprint, jsonify

bp = Blueprint("metadata", __name__, url_prefix="/metadata")

@bp.route("/", methods=["GET"])
def get_metadata():
    return jsonify({"model": "example_model", "version": "1.0.0"}), 200