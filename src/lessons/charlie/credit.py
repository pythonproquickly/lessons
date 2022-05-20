"""Perform credit card calculations."""
# #ANDY: import package to handle command line argument parsing
from argparse import ArgumentParser

# #ANDY: this is not needed
import sys


# #ANDY: define all functions using def. Thet will be called later when needed.

# #ANDY: this function takes two parameters: b and f. f defaults to a
# value of 0. The function can be called without specifying a value for f
def get_min_payment(b, f=0):
    """Calculates minimum credit card payment.

    Args:
      b (float or int): Balance in the account
      f (float or int): Amount of fees to be paid per month
      m (float): percent of balance to be paid

    Returns:
    g (float or int): Minimum credit card payment
    """

    m = 0.02
    g = (b * m) + f
    if g < 25:
        g = 25

    # #ANDY: function return the value g
    return g


# #ANDY: two parameters: a and b
def interest_charged(a, b):
    """Calculates interest charged.

    Args:
    b (float or int): Balance on the account
    a (int): Annual APR

    Returns:
      i (float or int): The amount of interest accrued in the next payment
    """

    y = 365
    apr = a / 100
    d = 30
    t = apr / y
    u = t * b
    i = u * d
    return i


# #ANDY: credit_line and a both have default values
def remaining_payments(balance, r, tp, credit_line=5000, a=0):
    """Calculates the remaining payments.

    Args:
      balance (float or int): The balance of the credit card
      r (int): Annual APR
      tp (float or int): The target payment
      credit_line (int): The credit line
      a (int): The amount of fees that will be charged in addition to the minimum payment.

    Returns:
      counter_p, counter_t, counter_f, counter_s (tuple): The number of payments required to pay off the credit card balance
    """
    counter_p = 0
    counter_t = 0
    counter_f = 0
    counter_s = 0
    # #ANDY: iterate reducing balance by principal on each iteration
    # this way, we calculate the payoff period

    while balance > 0:
        if tp == None:
            paymentamount = get_min_payment(balance, a)
        else:
            paymentamount = tp
        principal = paymentamount - interest_charged(r, balance)
        if principal < 0:
            print("The cards balance cannot be paid off")
            return
        # #ANDY this next bit calculates month data for the following output:
        """
        You will spend a total of 34 months over 25% of the credit line. 
        You will spend a total of 18 months over 50% of the credit line. 
        You will spend a total of 3 months over 75% of the credit line.

        """
        balance = balance - principal
        if balance >= 0.75 * credit_line:
            counter_s += 1
        if balance >= 0.5 * credit_line:
            counter_f += 1
        if balance >= 0.25 * credit_line:
            counter_t += 1
        counter_p += 1

    return counter_p, counter_t, counter_f, counter_s


# #ANDY: note use fo default parameters again
def main(b, apr, credit_line=5000, targetamount=None, fees=0):
    """Uses get_minimum and remaining payments functions to output credit card payment information to user.

    Args:
      b (int or float): Balance of credit card
      apr (int): Annual APR
      targetamount (float or int): The amount the user wants to pay per payment
      credit_line (int): The maximum amount of balance that an account holder can keep in their account.
      fees (int): The amount of fees that will be charged in addition to the minimum payment

    Returns:
      min_payment (float or int): Recommended minimum payment
      total_payments (tuple): Number of payments
      targetamount (float or int): Target payment amount
      A string that is a message that will tell the user how many payments they will be above 25, 50 and 75 percent thresholds
    """

    min_payment = get_min_payment(b, fees)
    print("The recommended minimum payment is: ", min_payment)
    pays_minimum = False
    if targetamount == None:
        pays_minimum = True
    elif targetamount < min_payment:
        print(
            "Your target payment is less than the minimum payment for this credit card"
        )
        return
    total_payments = remaining_payments(b, apr, targetamount, credit_line, fees)
    if pays_minimum == True:
        print(
            f"If you pay the minimum payments each month, you will pay off the balance in {total_payments[0]} payments."
        )
    if pays_minimum == False:
        print(
            f"If you make payments of {targetamount}, you will pay off the balance in {total_payments[0]} payments."
        )
    return f"You will spend a total of {total_payments[1]} months over 25% of the credit line. \n You will spend a total of {total_payments[2]} months over 50% of the credit line. \n You will spend a total of {total_payments[3]} months over 75% of the credit line."


# #ANDY: Here the program processes the command line arguments
# you provide the balance_amount value, apr value, credit_line value, payment
# value and fees value
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments

    Args:
      args_list (list) : the list of strings from the command prompt
    Returns:
      args (ArgumentParser)
    """
    # #ANDY: get the command line arguments
    parser = ArgumentParser()
    # #ANDY: define the arguments
    parser.add_argument(
        "balance_amount",
        type=float,
        help="The total amount of balance left on the credit account",
    )
    parser.add_argument(
        "apr", type=int, help="The annual APR, should be an int between 1 and 100"
    )
    parser.add_argument(
        "credit_line",
        type=int,
        help="The maximum amount of balance allowed on the credit line.",
    )
    parser.add_argument(
        "--payment",
        type=int,
        default=None,
        help="The amount the user wants to pay per payment, should be a positive number",
    )
    parser.add_argument(
        "--fees", type=float, default=0, help="The fees that are applied monthly."
    )

    # #ANDY: get the srguments values and set corresponding variables
    # raise errors if the values are invalid
    # parse and validate arguments
    args = parser.parse_args(args_list)

    if args.balance_amount < 0:
        # #ANDY: create an expection that is caught below - each follows same
        # pattern
        raise ValueError("balance amount must be positive")
    if not 0 <= args.apr <= 100:
        raise ValueError("APR must be between 0 and 100")
    if args.credit_line < 1:
        raise ValueError("credit line must be positive")
    if args.payment is not None and args.payment < 0:
        raise ValueError("number of payments per year must be positive")
    if args.fees < 0:
        raise ValueError("fees must be positive")

    return args


if __name__ == "__main__":
    try:
        # if an error is raised because of invalid parameter rasie excpetion...
        # otherwise the valid args are returned
        arguments = parse_args(sys.argv[1:])
    except ValueError as e:
        # #ANDY: catch exception and exit program
        sys.exit(str(e))

    # #ANDY: now we know the parameters are correct we can run
    # #ANDY: the valid args are passed to main
    print(
        main(
            arguments.balance_amount,
            arguments.apr,
            credit_line=arguments.credit_line,
            targetamount=arguments.payment,
            fees=arguments.fees,
        )
    )

    # #ANDY# comment out line 191 and uncomment what follows to see the
    # program run
    """result = main(40000.00, 2,
                  50000, 850,
                  5)

    print(result)"""
