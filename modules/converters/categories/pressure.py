FACTORS = {
    "pascal": 1,
    "bar": 100000,
    "psi": 6894.76,
    "atm": 101325,
    "torr": 133.322
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]