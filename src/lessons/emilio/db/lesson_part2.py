def get_input():
    data = {
        'account_no': {
            'prompt': "Enter the account number: ",
            'item_value': None},
        'balance': {
            'prompt': "Enter account balance: ",
            'item_value': None},
        'customer_credit': {
            'prompt': "Enter the customer credit: ",
            'item_value': None},
        'customer_name': {
            'prompt': "Enter the customer name: ",
            'item_value': None},
    }
    for field, field_data in data.items():
        field_data['item_value'] = input(field_data['prompt'])

    return data


def validate_account_no(account_number):
    if len(account_number) < 5:
        return False
    return True


def validate_balance(balance):
    if len(balance) < 5:
        return False
    return True


def validate_customer_credit(customer_credit):
    if len(customer_credit) < 5:
        return False
    return True


def validate_customer_name(customer_name):
    if len(customer_name) < 5:
        return False
    return True


def validate(unvalidated):
    unvalidated['account_no']['is_valid'] = False
    unvalidated['account_no']['validate'] = validate_account_no
    unvalidated['balance']['is_valid'] = False
    unvalidated['balance']['validate'] = validate_balance
    unvalidated['customer_credit']['is_valid'] = False
    unvalidated['customer_credit']['validate'] = validate_customer_credit
    unvalidated['customer_name']['is_valid'] = False
    unvalidated['customer_name']['validate'] = validate_customer_name
    for field, field_data in unvalidated.items():
        field_data['is_valid'] = \
            field_data['validate'](field_data['item_value'])

    return unvalidated


def main():
    mydata = get_input()
    my_valid_data = validate(mydata)
    print(my_valid_data)  # just to show


if __name__ == "__main__":
    main()
