def calculate_emi(data):
    principal = float(
        data["principal"]
    )

    annual_rate = float(
        data["rate"]
    )

    years = float(
        data["time"]
    )

    frequency = data.get(
        "frequency",
        "monthly"
    )

    frequency_map = {
        "weekly": 52,
        "bi-weekly": 26,
        "monthly": 12,
        "quarterly": 4,
        "half-yearly": 2,
        "yearly": 1,
    }

    periods_per_year = (
        frequency_map[frequency]
    )

    periodic_rate = (
        annual_rate
        / periods_per_year
        / 100
    )

    total_periods = (
        years * periods_per_year
    )

    emi = (
        principal
        * periodic_rate
        * (
            (1 + periodic_rate)
            ** total_periods
        )
    ) / (
        (
            (1 + periodic_rate)
            ** total_periods
        ) - 1
    )

    total_payment = (
        emi * total_periods
    )

    total_interest = (
        total_payment - principal
    )

    return {
        "emi": round(emi, 2),

        "total_payment": round(
            total_payment,
            2
        ),

        "total_interest": round(
            total_interest,
            2
        ),

        "frequency": frequency,
    }