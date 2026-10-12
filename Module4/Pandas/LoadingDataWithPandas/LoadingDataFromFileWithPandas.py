import pandas as pd
from Module4.Files.ReadingFilesWithOpen.DownloadFiles import download

download(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv",
    "Product-sales.csv"
)

download(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx",
    "Product-sales.xlsx"
)

print("Generating dataframe based on the downloaded csv file")
csv_df = pd.read_csv("Product-sales.csv")
print(csv_df)

print("Generating dataframe based on the downloaded xlsx file")
xlsx_df = pd.read_excel("Product-sales.xlsx")
print(xlsx_df)