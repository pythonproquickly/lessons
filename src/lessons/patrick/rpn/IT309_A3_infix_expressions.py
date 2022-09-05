# IT309 infix expressions to use for testing - not comprehensive

IFList = (
    "7 + 5 ",
    "7 - 5 ",
    "7 * 5 ",
    "15 / 5 ",
    "8 $ 4 ",
    "8 / 4 * 2 + 3 ",
    "8 / 4 + 2 * 3 ",
    "16 - 8 / 4 * 2 * 4 ",
    "100 * 100 / 20 + 55 ",
    "200 w * 10 +",
    "( 4 + 5 * 3 ) - 6",
    "( 3 * ( 4 + 5 ) + 6 ",
    "( ( 30 * 40 ) + 20 ) * 10 + 50 ",
)

# code to test that the expressions are correctly separated and can be parsed.
# also tests whether the individual parsed symbols are numbers.
# Do not include in the assignment submission.

for e in IFList:
    print("\nExpression: ", e)
    x = e.split(" ")
    for n in x:
        print(n, end=" ")
    print("")  # puts space between expression and first token
    for n in x:
        if n.isdigit():
            print(n, " is a number")
        else:
            print(n, " is a nonumeric symbol")
