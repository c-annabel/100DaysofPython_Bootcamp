#AI generated image https://www.thispersondoesnotexist.com/
# Only for reference, not workable, due to increased security check on Tinder


URL = "https://tinder.com"
ACCOUNT_ID = "id"
ACCOUNT_PW = "pw"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="../Development")
driver = webdriver.Chrome(options=options, service=service)
driver.get(URL)

sleep(2)
privacy = driver.find_element(By.XPATH, '//*[@id="c-60880778"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
privacy.click()
#

# Cybersecurity has implemented for Tinder, the exercise has been skipped,
# Below are some notes to be taken from the Solution

# Get all the window handles with
all_windows = driver.window_handles
# first window
base_window = driver.window_handles[0]
# Next window
fb_login_window = driver.window_handles[1]
# Switch window
driver.switch_to.window(fb_login_window)
# Print title
print(driver.title)
# Revert back to the base_window
driver.switch_to.window(base_window)

try:
    print("called")
    like_button= driver.find_element(By.XPATH, "match/button")
    like_button.send_keys(Keys.ENTER)
except ElementClickInterceptedException:
    try:
        match_popup= driver.find_element(By.CSS_SELECTOR, ".itsMatch a").click()
    except NoSuchElementException:
        pass

sleep(2)

driver.quit()
