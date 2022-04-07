from loguru import logger


def log_me(func):
    def inner(a, b):
        logger.info(f"{__name__} calculated with {a}, {b}")
        return func(a, b)

    return inner


@log_me
def calculate_amount(premium, interest):
    return premium * interest


def main():
    amount = calculate_amount(120, 1.10)
    print(f"\nAmount is {amount}")


if __name__ == "__main__":
    main()
