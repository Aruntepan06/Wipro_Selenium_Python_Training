from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"

headers = {

    # user - agent - who is making the request
    "User-Agent": "Chrome/144.0.7559.133"
}

response = requests.get(url, headers=headers)
print(response.status_code)
# parse the html
soup = BeautifulSoup(response.text, features="html.parser")

# html code is printed
print(soup)
# get the title of the page
print(soup.title.string)
# get the first matching tag
print(soup.find("h1"))
# get the first matching paragraph
print(soup.find("p"))

# head
headtag = soup.head
print(headtag.contents)


# get the title of the page
print(soup.title.string)

#to get all the link
links = soup.find_all("a")

for link in links:
    print(link.get("href"))

# get the first matching tag
print(soup.find("h1"))

# get the matching paragraph
print(soup.find("p"))



# extract the book
books = soup.find_all(name= "article", class_ = "product_pod")

# extract title and price in the books
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_ = "price_color").text
    print("Title:", title)
    print("Price", price)


html_doc = """
<html>
<head>
    <title>List Example</title>
</head>
<body>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, features="html.parser")

# finding the <li> tags
items = soup.find_all('li')

for item in items:
    print(item.text)



html_doc = """
<html>
<head><title>CSS Selector Example</title></head>
<body>
  <div id="main">
    <p class="info">Info Paragraph 1</p>
    <p class="info">Info Paragraph 2</p>
  </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, features="html.parser")

items = soup.find_all('p')
for item in items:
    print(item.text)