def validate_quantity(quantity):
    if quantity > 0:
        return True
    return False


def validate_bk():
    return False


booking = {
    "quantity": {
        "value": None,
        "prompt": "Please enter the quantity to book",
        "validation_function": validate_quantity,
    },
    "booking_number": {
        "value": None,
        "prompt": "Enter booking number",
        "validation_function": validate_bk,
    },
}

for field_name, field_details in booking.items():
    field_details["value"] = input(field_details["prompt"])
    print(field_details["value"])

