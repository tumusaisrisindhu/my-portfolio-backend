FACTORS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34,
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]