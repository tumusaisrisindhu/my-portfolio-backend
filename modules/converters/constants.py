from .categories import (
    length,
    weight,
    temperature,
    distance,
    volume,
    area,
    time,
    speed,
    pressure,
    energy,
    data,
    number_system
)

CONVERTER_CONFIG = {
    "length": list(length.FACTORS.keys()),
    "weight": list(weight.FACTORS.keys()),
    "temperature": ["celsius", "fahrenheit", "kelvin"],
    "distance": list(distance.FACTORS.keys()),
    "volume": list(volume.FACTORS.keys()),
    "area": list(area.FACTORS.keys()),
    "time": list(time.FACTORS.keys()),
    "speed": list(speed.FACTORS.keys()),
    "pressure": list(pressure.FACTORS.keys()),
    "energy": list(energy.FACTORS.keys()),
    "data_storage": list(data.FACTORS.keys()),
    "number_system": list(number_system.MAP.keys()),
}