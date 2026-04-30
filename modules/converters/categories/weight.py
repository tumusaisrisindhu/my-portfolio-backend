FACTORS = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "tonne": 1_000_000,
    "ounce": 28.3495,
    "pound": 453.592,
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]