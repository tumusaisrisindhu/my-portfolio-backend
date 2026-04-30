MAP = {
    "thousand": 1e3,
    "lakh": 1e5,
    "crore": 1e7,
    "arab": 1e9,

    "million": 1e6,
    "billion": 1e9,
    "trillion": 1e12
}

def convert(value, from_unit, to_unit):
    base = value * MAP[from_unit]
    return base / MAP[to_unit]