FACTORS = {
    "millisecond": 0.001,
    "second": 1,
    "minute": 60,
    "hour": 3600,
    "day": 86400,
    "week": 604800,
    "month": 2629800,   # approx
    "year": 31557600    # approx
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]