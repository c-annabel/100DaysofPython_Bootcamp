URL_ZILLOW = "ZILLOW LINK"

ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"
ACCEPT_LANGUAGE = "en-GB,en;q=0.9"

URL_FORM = "GOOGLE FORM LINK HERE"

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import requests
import pprint

sleep(0.1)

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}


response = requests.get(url=URL_ZILLOW, headers=headers)
zl_web_page = response.text
soup = BeautifulSoup(zl_web_page, "html.parser")
list_urls = soup.select("div.property-card-data a")
#Only managed to scrape 9 records at once.
all_links = []
all_addresses = []
for link in list_urls:
    href = link["href"]
    address = link.getText()
    if "http" not in href:
        all_links.append(f"https://www.zillow.com/{href}")
    else:
        all_links.append(href)
    all_addresses.append(address.split("|")[-1])

list_prices = soup.select("div.property-card-data div.bqsBln span")
all_prices = [(price.getText().split("+")[0]) for price in list_prices if "$" in price.text]

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="../Development")
driver = webdriver.Chrome(options=options, service=service)

for n in range(len(all_links)):
    driver.get(URL_FORM)
    sleep(2)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit.click()

    sleep(1)

