FACTORS = {
    "joule": 1,
    "kilojoule": 1000,

    "calorie": 4.184,
    "kilocalorie": 4184,

    "watt_hour": 3600,
    "kwh": 3_600_000
}

def convert(value, from_unit, to_unit):
    base = value * FACTORS[from_unit]
    return base / FACTORS[to_unit]