from bs4 import BeautifulSoup
import requests

# 1) Parse HTML – Extract title and h1
html = '''
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<p>This is a paragraph.</p>
</body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")

title_text = soup.title.get_text(strip=True) if soup.title else None
h1_text = soup.find("h1").get_text(strip=True) if soup.find("h1") else None

print("1) Title:", title_text)
print("1) H1:", h1_text)

# 2) Extract All Paragraphs
paras = [p.get_text(strip=True) for p in soup.find_all("p")]
print("\n2) Paragraphs:", paras)

# 3) Extract All Links and Count
links = soup.find_all("a")
print("\n3) Links count:", len(links))
print("3) Links text:", [a.get_text(strip=True) for a in links])

# 4) Extract Attributes (just showing tags that actually have attributes)
attr_list = []
for tag in soup.find_all(True):
    if tag.attrs:
        attr_list.append((tag.name, tag.attrs))
print("\n4) Tag attributes:", attr_list)

# 5) Extract First h2
first_h2 = soup.find("h2")
print("\n5) First H2:", first_h2.get_text(strip=True) if first_h2 else None)

# 6) Extract Bold Text (b and strong)
bold_texts = [t.get_text(strip=True) for t in soup.find_all(["b", "strong"])]
print("\n6) Bold texts:", bold_texts)

# 7) Extract All href Values
hrefs = [a.get("href") for a in soup.find_all("a") if a.get("href")]
print("\n7) All hrefs:", hrefs)

# 8) Get All Text Without Tags
all_text = soup.get_text(separator=" ", strip=True)
print("\n8) All text:", all_text)

# 9) Extract Title from Website
def get_website_title(url: str):
    # simple request with a user-agent so some sites don’t block it
    res = requests.get(url, timeout=15, headers={"User-Agent": "Chrome/145.0.7632.68"})
    res.raise_for_status()
    s = BeautifulSoup(res.text, "html.parser")
    return s.title.get_text(strip=True) if s.title else None

# example:
print("\n9) Website title:", get_website_title("https://jsonplaceholder.typicode.com/"))

# 10) Extract All Headings (h1-h6)
headings = []
for level in range(1, 7):
    for tag in soup.find_all(f"h{level}"):
        headings.append((tag.name, tag.get_text(strip=True)))
print("\n10) Headings:", headings)

# 11) Extract Table Data
table_html = """
<table>
  <tr><th>Name</th><th>Age</th></tr>
  <tr><td>Arun</td><td>24</td></tr>
  <tr><td>Neha</td><td>22</td></tr>
</table>
"""
table_soup = BeautifulSoup(table_html, "html.parser")
table = table_soup.find("table")

table_rows = []
if table:
    for tr in table.find_all("tr"):
        cells = tr.find_all(["th", "td"])
        table_rows.append([c.get_text(strip=True) for c in cells])

print("\n11) Table rows:", table_rows)

# 12) Extract Images
img_html = """
<div>
  <img src="a.jpg" alt="A">
  <img src="/images/b.png">
</div>
"""
img_soup = BeautifulSoup(img_html, "html.parser")
images = [{"src": img.get("src"), "alt": img.get("alt")} for img in img_soup.find_all("img")]
print("\n12) Images:", images)
