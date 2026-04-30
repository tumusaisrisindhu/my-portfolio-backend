def convert(value, from_unit, to_unit):
    # to celsius
    if from_unit == "fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "kelvin":
        value = value - 273.15

    # to target
    if to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "kelvin":
        return value + 273.15

    return value