from flask import Blueprint, jsonify

from .service import (
    generate_number_service,
    get_history_service,
    reset_game_service
)

housie_bp = Blueprint("housie", __name__)


# 🎲 GENERATE NUMBER
@housie_bp.route("/housie/generate", methods=["POST"])
def generate_number():
    result = generate_number_service()

    return jsonify(result)


# 📜 HISTORY
@housie_bp.route("/housie/history", methods=["GET"])
def get_history():
    history = get_history_service()

    return jsonify(history)


# 🔄 RESET
@housie_bp.route("/housie/reset", methods=["POST"])
def reset_game():
    result = reset_game_service()

    return jsonify(result)