# IT309 postfix expressions to use for testing Part 1 of the assignment - not comprehensive

PFList = (
    "7 5 +",
    "7 5 -",
    "7 5 *",
    "7 5 /",
    "8 4 @",
    "8 4 / 2 * 3 +",
    "8 4 / 2 * 3 *",
    "6 8 4 / 2 * 4 + -",
    "100 100 * 20 /",
    "200 w * 10 +",
    "7 6 15 11 2 * + * 20 + -",
    "3 4 5 * + * 6 + ",
    "10 20 30 40 * + * 50 +",
)

# code to test that the expressions are correctly separated and can be parsed.
# Do not include in the assignment submission.

for ex in PFList:
    print("Input expression:        \t", ex)
    x = ex.split(" ")
    print("Converted to a list:     \t", x)
    print("Parsed expression terms: \t", end=" ")
    for n in x:
        print(n, end=" ")
    print("\n")  # put space after last expression
