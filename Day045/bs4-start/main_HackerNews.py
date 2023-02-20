# https://news.ycombinator.com

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a")



# article_text = articles.getText()
# article_link = articles.get("href")
# article_upvotes = soup.find_all(name="span", class_="score").getText()
#
# print(article_text)
# print(article_link)
# print(article_upvote)
