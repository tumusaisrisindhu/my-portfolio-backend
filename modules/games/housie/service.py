from .engine import pick_random_number, get_history, reset_game


def generate_number_service():
    return pick_random_number()


def get_history_service():
    return get_history()


def reset_game_service():
    return reset_game()