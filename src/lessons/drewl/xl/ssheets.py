# pip install openpyxl
import pandas as pd
prods = pd.read_excel('products.xlsx', index_col=0, header=[0])
prods.columns = prods.iloc[0]
prods = prods.iloc[1:].reset_index(drop=True)
print(prods)
