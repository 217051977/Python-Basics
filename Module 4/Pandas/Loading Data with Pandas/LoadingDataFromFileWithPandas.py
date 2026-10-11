import pandas as pd

print("Generating dataframe based on the downloaded csv file")
csv_df = pd.read_csv("Product-sales.csv")
print(csv_df)

print("Generating dataframe based on the downloaded xlsx file")
xlsx_df = pd.read_excel("Product-sales.xlsx")
print(xlsx_df)