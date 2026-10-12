from bs4 import BeautifulSoup

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html.parser')
print("Getting prettified html:", soup.prettify())

print("\nGetting Tag objects:")
print("Tile:", soup.title, f" ({type(soup.title)})")
print("Getting children:", soup.h3.b)
print("Getting parent:", soup.h3.parent)
print("Getting sibling:", soup.h3.next_sibling)
print("Getting sibling of the sibling:", soup.h3.next_sibling.next_sibling)
print(f"Getting html attribute: {soup.h3.b['id']} or {soup.h3.b.attrs} or {soup.h3.b.get('id')}")
print(f"Getting navigable String: {soup.h3.b.string} ({type(soup.h3.b.string)})")
print(f"Getting unicode of the navigable String: {str(soup.h3.b.string)} ({type(str(soup.h3.b.string))})")
