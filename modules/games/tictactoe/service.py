from .game_state import game_state
from .utils import check_winner, check_tie


def get_game_state():
    return game_state


def make_move(index):
    if game_state["winner"] or game_state["is_tie"]:
        return game_state

    if game_state["board"][index] != "":
        return game_state

    current_player = game_state["current_player"]

    game_state["board"][index] = current_player

    winner = check_winner(game_state["board"])

    if winner:
        game_state["winner"] = winner

    elif check_tie(game_state["board"]):
        game_state["is_tie"] = True

    else:
        game_state["current_player"] = (
            "O" if current_player == "X" else "X"
        )

    return game_state


def reset_game():
    game_state["board"] = ["", "", "", "", "", "", "", "", ""]
    game_state["current_player"] = "X"
    game_state["winner"] = None
    game_state["is_tie"] = False

    return game_state


def update_player_name(symbol, name):
    game_state["players"][symbol] = name

    return game_state