def addup(lhs, rhs):
    return lhs + rhs


def subit(lhs, rhs):
    return lhs - rhs


assert addup(9, 2) == 11
assert subit(5, 2) == 3


def calculate(f, lhs, rhs):
    return f(lhs, rhs)


assert calculate(addup, 3, 4) == 7
assert calculate(subit, 3, 4) == -1



def is_number_valid(booking_num):
    return True


booking = {
    '1234': {'prompt': 'Please enter booking number: ',
             'validate': is_number_valid,
             'value': None}
}

for booking_number, shipment_details in booking.items():
    shipment_details['value'] = input(shipment_details['prompt'])
    assert shipment_details['validate'](shipment_details['value']) is False

print(shipment_details)


