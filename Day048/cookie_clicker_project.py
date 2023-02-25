#https://orteil.dashnet.org/cookieclicker/

# URL="https://orteil.dashnet.org/cookieclicker/"
URL="http://orteil.dashnet.org/experiments/cookie/"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="../Development")
driver = webdriver.Chrome(options=options, service=service)
driver.get(URL)

# consent = driver.find_element(By.CSS_SELECTOR, ".fc-footer-buttons button.fc-button")
# consent.click()
# language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
# language.click()
# the_cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
# the_cookie.click()

cookie = driver.find_element(By.CSS_SELECTOR, "div#cookie")
prizes = driver.find_elements(By.CSS_SELECTOR, "div#store div.grayed b")
#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

prize_dict={}
for n in range(len(prizes)-1):
    item_detail = prizes[n].text.strip().split("-")
    money = item_detail[1].strip().replace(",","")
    prize_dict[n] = {
        # "Item": item_detail[0].strip(),
        "Item": item_ids[n],
        "Money": int(money),
    }

timeout = time.time()+2 #2 seconds
one_min = time.time() + 60 * 1 # 1 minutes

def cookie_upgrade():
    for n in range(len(prize_dict) - 1, -1, -1):
        prize_cost = prize_dict[n]["Money"]
        if current_money >= prize_cost:
            # item_id = "buy"+ prize_dict[n]["Item"]
            buy_item = driver.find_element(By.CSS_SELECTOR, f"div#{prize_dict[n]['Item']}")
            buy_item.click()
            break

while True:
    cookie.click()

    if time.time() > timeout:
        time.sleep(1)
        earned_cookies = driver.find_element(By.CSS_SELECTOR, "div#game div#money")
        current_money = int(earned_cookies.text)

        cookie_upgrade()

        timeout = time.time() + 2

    if time.time() > one_min:
        time.sleep(1)
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break

















