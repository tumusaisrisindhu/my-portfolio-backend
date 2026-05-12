def calculate_simple_interest(data):
    principal = float(data["principal"])
    rate = float(data["rate"])
    time = float(data["time"])

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