from bs4 import BeautifulSoup

html="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

soup = BeautifulSoup(html, 'html.parser')
print("Getting prettified html:", soup.prettify())

print("\nUsing 'Find All' to filter by name:", (type(soup.find_all('tr'))), soup.find_all('tr'))
print("Getting the first element of the table row:", (type(soup.find_all('tr')[0])), soup.find_all('tr')[0])
print("Getting the table row child:", (type(soup.find_all('tr')[0].td)), soup.find_all('tr')[0].td)
print("Iterate through the table:")
for i, row in enumerate(soup.find_all('tr')):
    print("row", i, "is", row)
print("Iterate through each table rows:")
for i, row in enumerate(soup.find_all('tr')):
    print("row", i, "is", row)
    for j, cell in enumerate(row.find_all('td')):
        print("\tcolumn", j, "is", cell)

print("\nUsing 'Find All' to filter by attribute:")
print("id:", soup.find_all(id = 'flight'))
print("href:", soup.find_all(href = "https://en.wikipedia.org/wiki/Florida"))
print("has href:", soup.find_all(href = True))

print("\nUsing 'Find All' to filter by string:")
print("id:", soup.find_all(string = 'Florida'))

print("\nUsing 'Find' to filter by name:", (type(soup.find_all('tr'))), soup.find_all('tr'))
print("Getting the first element of the table row:", (type(soup.find_all('tr')[0])), soup.find_all('tr')[0])
print("Getting the table row child:", (type(soup.find_all('tr')[0].td)), soup.find_all('tr')[0].td)
print("Iterate through the table:")
for i, row in enumerate(soup.find_all('tr')):
    print("row", i, "is", row)
print("Iterate through each table rows:")
for i, row in enumerate(soup.find_all('tr')):
    print("row", i, "is", row)
    for j, cell in enumerate(row.find_all('td')):
        print("\tcolumn", j, "is", cell)