def validate_quantity(quantity):
    quantity = int(quantity)
    if quantity > 0:
        return True
    return False


def validate_bk(dummy):
    return False


def validate_destination(dummy):
    return True


booking = {
    "booking_number": {
        "value": None,
        "prompt": "Enter booking number",
        "validation_function": validate_bk,
    },
    "quantity": {
        "value": None,
        "prompt": "Please enter the quantity to book",
        "validation_function": validate_quantity,
    },
    "destination": {
        "value": None,
        "prompt": "Please enter where it's going",
        "validation_function": validate_destination,
    },
}

for field_name, field_details in booking.items():
    field_details["value"] = input(field_details["prompt"])
    isvalid = field_details["validation_function"](field_details["value"])
    print(isvalid)
