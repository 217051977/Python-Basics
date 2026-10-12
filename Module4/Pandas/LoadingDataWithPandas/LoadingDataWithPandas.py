import pandas as pd

print("Generating dataframe based on the downloaded csv file")
df = pd.read_csv("Product-sales.csv")
print(df)

print("\nRetrieve the first 2 lines")
print(df.head(2))

print("\nRetrieve the column 'Category' as series")
cs = df['Category']
print(cs)

print("\nPrinting column 'Category' as series type")
print(type(cs))

print("\nRetrieve first row from the frist column using 'iloc'")
fr_fc = df.iloc[0, 0]
print(fr_fc)

print("\nRetrieve second row from the frist column using 'iloc'")
sr_fc = df.iloc[1, 0]
print(sr_fc)

print("\nRetrieve first row from the 'Product' column using 'loc'")
fr_pc = df.loc[0, 'Product']
print(fr_pc)

print("\nRetrieve second row from the 'Product' column using 'loc'")
sr_pc = df.loc[1, 'Product']
print(sr_pc)

print("\nRetrieve sub dataframe / Slicing dataframe using 'iloc'")
sdf_iloc = df.iloc[0:2, 0:3]
print(sdf_iloc)

print("\nRetrieve sub dataframe / Slicing dataframe using 'loc'")
sdf_loc = df.loc[0:2, 'OrderID':'Category']
print(sdf_loc)