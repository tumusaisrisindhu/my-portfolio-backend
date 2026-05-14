def convert_to_years(time, tenure_type):
    time = float(time)

    conversions = {
        "days": time / 365,
        "months": time / 12,
        "years": time,
    }

    return conversions.get(
        tenure_type,
        time
    )


def get_compound_frequency(frequency_type):
    frequencies = {
        "daily": 365,
        "monthly": 12,
        "quarterly": 4,
        "half-yearly": 2,
        "yearly": 1,
    }

    return frequencies.get(
        frequency_type,
        1
    )


def calculate_compound_interest(data):
    principal = float(
        data["principal"]
    )

    rate = (
        float(data["rate"]) / 100
    )

    tenure_type = data[
        "tenure_type"
    ]

    frequency_type = data[
        "frequency_type"
    ]

    time = convert_to_years(
        data["time"],
        tenure_type
    )

    frequency = get_compound_frequency(
        frequency_type
    )

    total_amount = principal * (
        (
            1 +
            (rate / frequency)
        ) ** (frequency * time)
    )

    compound_interest = (
        total_amount - principal
    )

    return {
        "compound_interest": round(
            compound_interest,
            2
        ),

        "total_amount": round(
            total_amount,
            2
        )
    }