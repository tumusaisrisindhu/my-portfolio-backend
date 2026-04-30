from .engine import convert_value
from .constants import CONVERTER_CONFIG


def get_converter_config():
    return CONVERTER_CONFIG


def perform_conversion(data):
    value = float(data["value"])
    category = data["category"]
    from_unit = data["from_unit"]
    to_unit = data["to_unit"]

    result = convert_value(category, value, from_unit, to_unit)

    return result