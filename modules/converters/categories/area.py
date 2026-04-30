FACTORS = {
    "sq_mm": 1e-6,
    "sq_cm": 1e-4,
    "sq_m": 1,
    "sq_km": 1e6,

    "sq_ft": 0.092903,
    "sq_yd": 0.836127,

    "hectare": 10000,
    "acre": 4046.86
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]