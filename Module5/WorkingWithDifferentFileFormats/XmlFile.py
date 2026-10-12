import xml.etree.ElementTree as ET
from Module4.Files.ReadingFilesWithOpen.DownloadFiles import download
import pandas as pd

employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("Sample-employee-XML-file.xml", "wb") as files:
    mydata1.write(files)

download(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml',
    'Sample-employee-XML-file.xml'
)

tree = ET.parse("Sample-employee-XML-file.xml")

# Get the root of the XML tree
root = tree.getroot()

# Define the columns for the DataFrame
columns = ["firstname", "lastname", "title", "division", "building", "room"]

# Collect one row (a list of values) per employee
rows = []
for node in root:
    rows.append([node.find(col).text for col in columns])

# Create the DataFrame once from the collected rows
df = pd.DataFrame(rows, columns=columns)

print(df)
