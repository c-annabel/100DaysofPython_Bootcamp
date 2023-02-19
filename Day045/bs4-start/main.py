# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a) #first a tag

# print(soup.find_all(name="a"))

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name") #only find the first item that matches
# print(heading)

section_heading = soup.find(name="h3", class_="heading") #class_ to avoid preserved word
# print(section_heading)
# print(section_heading.get("class"))
# print(section_heading.getText())

company_url = soup.select_one(selector="p a") #a tag is sit inside a p tag
# print(company_url)
name = soup.select_one(selector="#name") # [#name] => id="name"
# print(name)

headings = soup.select(".heading") # [.heading] => class = "heading"
print(headings)