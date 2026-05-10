from flask import Blueprint, jsonify, request

from .service import (
    get_game_state,
    make_move,
    reset_game,
    update_player_name
)

tic_tac_toe_bp = Blueprint(
    "tic_tac_toe",
    __name__,
    url_prefix="/api/tic-tac-toe"
)


@tic_tac_toe_bp.route("/state", methods=["GET"])
def state():
    return jsonify(get_game_state())


@tic_tac_toe_bp.route("/move", methods=["POST"])
def move():
    data = request.get_json()

    index = data.get("index")

    updated_state = make_move(index)

    return jsonify(updated_state)


@tic_tac_toe_bp.route("/reset", methods=["POST"])
def reset():
    return jsonify(reset_game())


@tic_tac_toe_bp.route("/player", methods=["POST"])
def player():
    data = request.get_json()

    symbol = data.get("symbol")
    name = data.get("name")

    updated_state = update_player_name(symbol, name)

    return jsonify(updated_state)