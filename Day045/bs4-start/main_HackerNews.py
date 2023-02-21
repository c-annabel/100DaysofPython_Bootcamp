# https://news.ycombinator.com

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all(name="a")
articles = soup.select(selector="span.titleline a")

article_texts = []
article_links = []

for article_tag in articles:
    if article_tag.get("href")[0:4] == "from" or \
            article_tag.get("href")[0:4] == "item":
        pass
    else:
        text = article_tag.getText()
        article_texts.append(text)
        link = article_tag.get("href")
        article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
# print(largest_index)
# print(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])