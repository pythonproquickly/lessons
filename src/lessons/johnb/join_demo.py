# importing the module
import pandas as pd


def display_substitute(something):
    print(str(something))


display = display_substitute


df1 = pd.DataFrame({"fruit": ["apple", "banana", "avocado"],
                    "market_price": [21, 14, 35]})
display("The first DataFrame")
display(df1)


df2 = pd.DataFrame({"fruit": ["banana", "apple", "avocado"],
                    "wholesaler_price": [65, 68, 75]})
display("The second DataFrame")
display(df2)

display("The merged DataFrame")
pd.merge(df1, df2, on="fruit", how="inner")
