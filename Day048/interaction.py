#https://en.wikipedia.org/wiki/Main_Page

# URL="https://en.wikipedia.org/wiki/Main_Page"
URL="https://id.heroku.com/login"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="../Development")
driver = webdriver.Chrome(options=options, service=service)

driver.get(URL)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
# print(article_count)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

#Challenge_01
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python" + Keys.ENTER)
# search.clear()

#Challenge_02
email = driver.find_element(By.NAME, "email")
email.send_keys("name@email.com")
pw = driver.find_element(By.NAME, "password")
pw.send_keys("password")
# submit = driver.find_element(By.XPATH, '//*[@id="login"]/form/button')
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

# driver.quit()

