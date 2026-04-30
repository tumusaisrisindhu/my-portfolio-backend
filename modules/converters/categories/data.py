FACTORS = {
    "bit": 1,
    "byte": 8,

    "kb": 8 * 1e3,
    "mb": 8 * 1e6,
    "gb": 8 * 1e9,
    "tb": 8 * 1e12,

    "kib": 8 * 1024,
    "mib": 8 * 1024**2,
    "gib": 8 * 1024**3
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]