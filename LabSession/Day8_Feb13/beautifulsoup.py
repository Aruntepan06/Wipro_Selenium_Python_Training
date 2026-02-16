from bs4 import BeautifulSoup

import requests
from urllib.parse import urljoin


html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click Here</a>
  </body>
</html>
"""

# parse the html
soup = BeautifulSoup(html_doc, "html.parser")

# Extract the title text
print("Title:", soup.title.string)

# Extract the <h1> text
print("H1:", soup.find("h1").text)

# Extract the paragraph text
print("Paragraph:", soup.find("p").text)

# Find the first <a> tag
link = soup.find("a")
print("First Link Tag:", link)

# Print its href attribute
print("Href:", link.get("href"))

# Use prettify to format parsed HTML
print("\nFormatted HTML:\n")
print(soup.prettify())


# Difference
# find() → returns first matching element
# find_all() → returns all matching elements as a list

# Q2

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers, timeout=10)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

products = soup.find_all("article", class_="product_pod")

print("Product details\n")

for p in products:
    name = p.find("h3").find("a").get("title", "").strip()

    price = p.find("p", class_="price_color")
    price = price.get_text(strip=True) if price else ""

    availability = p.find("p", class_="instock availability")
    availability = availability.get_text(" ", strip=True) if availability else ""

    rating_tag = p.find("p", class_="star-rating")
    rating = ""
    if rating_tag:
        classes = rating_tag.get("class", [])
        rating = next((c for c in classes if c != "star-rating"), "")

    print("Name:", name)
    print("Price:", price)
    print("Rating:", rating)
    print("Availability:", availability)
    print("-" * 40)

print("\nAll image URLs\n")

image_urls = []
for img in soup.find_all("img"):
    src = img.get("src")
    if src:
        image_urls.append(urljoin(url, src))

for u in image_urls:
    print(u)