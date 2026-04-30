FACTORS = {
    "ml": 0.001,
    "liter": 1,
    "cubic_meter": 1000,

    "teaspoon": 0.00492892,
    "tablespoon": 0.0147868,
    "cup": 0.24,

    "pint": 0.473176,
    "quart": 0.946353,
    "gallon": 3.78541
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]