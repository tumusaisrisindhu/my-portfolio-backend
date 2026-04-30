FACTORS = {
    "m/s": 1,
    "km/h": 0.277778,
    "mph": 0.44704,
    "knot": 0.514444
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]