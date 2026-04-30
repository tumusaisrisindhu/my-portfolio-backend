from flask import Blueprint, request, jsonify 
from .service import get_converter_config, perform_conversion

converter_bp = Blueprint("converter", __name__)


@converter_bp.route("/converter-config", methods=["GET"])
def get_config():
    return jsonify(get_converter_config())


@converter_bp.route("/convert", methods=["POST"])
def convert():
    try:
        data = request.json
        result = perform_conversion(data)

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400