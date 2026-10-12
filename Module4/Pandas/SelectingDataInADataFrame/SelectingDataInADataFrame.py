import pandas as pd

dic = {
    'Name': [
        'Rose',
        'John',
        'Jane',
        'Mary'
    ],
    'ID': [
        1,
        2,
        3,
        4
    ],
    'Department': [
        'Architect Group',
        'Software Group',
        'Design Team',
        'Infrastructure'
    ],
    'Salary': [
        100000,
        80000,
        50000,
        60000
    ]
}

print("Generating dataframe based on the dictionary")
df = pd.DataFrame(dic)

print("\nPrinting dataframe")
print(df)

print("\nRetrieve the column 'ID'")
ids = df[['ID']]

print("\nPrinting column 'ID'")
print(ids)

print("\nPrinting column 'ID' type")
print(type(ids))

print("\nRetrieve sub dataframe")
sdf = df[['ID', 'Department', 'Salary']]

print("\nPrinting column 'ID'")
print(sdf)