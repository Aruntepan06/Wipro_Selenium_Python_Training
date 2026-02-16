import requests
from lxml import html

url = "https://lxml.de//"

response = requests.get(url)

# parse the HTML content
data = html.fromstring(response.content)

print(data)

title=data.find(".//title").text
print(title)

# // links
links = data.xpath("//a/@href")
print (title)

#links + URLS
links = data. xpath("//a")
for link in links:
    print(link.text)
    print (link.get("href"))

# extract the data using class name
titlelines = data.xpath("//span[@class='titleline']/a/text()")

for title in titlelines:
    print(title)
