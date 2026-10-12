from Module4.Files.ReadingFilesWithOpen.DownloadFiles import download
import pandas as pd

download(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv',
    'addresses.csv'
)

df = pd.read_csv("addresses.csv", header=None)
print("Save file content as a dataframe\n", df)

df.columns = ['First Name', 'Last Name', 'Location ', 'City', 'State', 'Area Code']
print("\nAdd headers to the columns\n", df)
