from .categories import length, weight, temperature, distance, volume, area, time, speed, pressure, energy, data, number_system

HANDLERS = {
    "length": length.convert,
    "weight": weight.convert,
    "temperature": temperature.convert,
    "distance": distance.convert,
    "volume": volume.convert,
    "area": area.convert,
    "time": time.convert,
    "speed": speed.convert,
    "pressure": pressure.convert,
    "energy": energy.convert,
    "data_storage": data.convert,
    "number_system": number_system.convert,
}

def convert_value(category, value, from_unit, to_unit):
    if category not in HANDLERS:
        raise ValueError(f"Unsupported category: {category}")

    return HANDLERS[category](value, from_unit, to_unit)