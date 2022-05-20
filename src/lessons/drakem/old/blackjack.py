import random
import sys


def get_card():
    return random.randint(1, 13)


def score(cards):
    return total, soft_ace_count


def stand(stand_on_value, stand_on_soft, cards):
    total, soft_ace_count = score(cards)
    # TODO: fill this in
    return True or False


def print_arg_error():
    print(
        "usage: blackjack.py <num-simulations> <stand-on-value (1-20)>"
        " <'soft'|'hard'>'"
    )


def main(args):
    strategy = args[2]
    try:
        num_simulations = int(args[0])
        stand_on_value = int(args[1])
    except ValueError:
        print_arg_error()
    if (
        strategy not in ("soft", "hard")
        or not (1 <= stand_on_value <= 20)
        or not (num_simulations > 0)
    ):
        print_arg_error()
        raise ValueError


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print_arg_error()
        exit()
    main(sys.argv[1:])
