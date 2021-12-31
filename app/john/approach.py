import data_defs


def get_input(data_items):
    pass


def validate(data_items):
    pass


def correct(data_items):
    while True:
        for field in data_items.items():
            if not field["is_valid"]:
                pass
                # what now?


def main():
    entered = get_input(data_defs.data_items)
    validated = validate(entered)
    corrected = correct(validated)


if __name__ == "__main__":
    main()
