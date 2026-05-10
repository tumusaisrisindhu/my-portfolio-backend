import random

from .state import generated_numbers, remaining_numbers


def pick_random_number():
    if not remaining_numbers:
        return None

    number = random.choice(remaining_numbers)

    remaining_numbers.remove(number)
    generated_numbers.append(number)

    return {
        "current_number": number,
        "last_five": generated_numbers[-5:][::-1],
        "generated_numbers": generated_numbers,
        "remaining_count": len(remaining_numbers),
    }


def get_history():
    return generated_numbers[::-1]


def reset_game():
    generated_numbers.clear()

    remaining_numbers.clear()
    remaining_numbers.extend(range(1, 91))

    return {
        "success": True
    }