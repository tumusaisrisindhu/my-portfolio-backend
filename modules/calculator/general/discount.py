def calculate_discount(data):
    original_price = float(data["original_price"])
    discount_value = float(data["discount_value"])
    discount_type = data["discount_type"]

    if discount_type == "percentage":
        discount_amount = (original_price * discount_value) / 100
    else:
        discount_amount = discount_value

    final_price = original_price - discount_amount

    return {
        "discount_amount": round(discount_amount, 2),
        "final_price": round(final_price, 2)
    }
