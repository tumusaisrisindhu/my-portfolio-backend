def convert_to_years(time, tenure_type):
    time = float(time)

    conversions = {
        "days": time / 365,
        "months": time / 12,
        "quarterly": time / 4,
        "half-yearly": time / 2,
        "yearly": time
    }

    return conversions.get(
        tenure_type,
        time
    )

def calculate_simple_interest(data):
    principal = float(
        data["principal"]
    )

    rate = float(
        data["rate"]
    )

    time = convert_to_years(
        data["time"],
        data["tenure_type"]
    )

    simple_interest = (
        principal * rate * time
    ) / 100

    total_amount = (
        principal + simple_interest
    )

    return {
        "simple_interest": round(
            simple_interest,
            2
        ),

        "total_amount": round(
            total_amount,
            2
        )
    }