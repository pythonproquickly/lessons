def get_input():
    my_input = dict()
    my_input["name"] = input("what is your name: ")
    return my_input

def validate_name_data(raw_name_data):
    if raw_name_data["name"] == "andy":


name_data = get_input()
good_name_data = validate_name_data(name_data)
