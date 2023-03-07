#https://www.google.com/search?q=how+to+scroll+popup+selnium+python&oq=how+to+scroll+popup+selnium+python&aqs=chrome..69i57j0.19371j0j9&sourceid=chrome&ie=UTF-8
#https://stackoverflow.com/questions/38041974/selenium-scroll-inside-of-popup-div
#https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop
#https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight

URL_IG = "https://instagram.com/"


TARGET_ACCOUNT = "target account"
IG_ID = "ID"
IG_PASSWORD = "pw"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class InstaFollower:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.service = Service(executable_path="../Development")
        self.driver = webdriver.Chrome(options=self.options, service=self.service)

    def login(self):
        self.driver.get(URL_IG)
        allow_cookie = self.driver.find_element(By.CSS_SELECTOR, '.x7r02ix button._a9_0')
        allow_cookie.click()
        sleep(3)
        input_username = self.driver.find_element(By.NAME, 'username')
        input_username.send_keys(IG_ID)
        input_password = self.driver.find_element(By.NAME, 'password')
        input_password.send_keys(IG_PASSWORD)
        input_password.send_keys(Keys.ENTER)
        sleep(6)
        save_info = self.driver.find_element(By.CSS_SELECTOR, '._aa56 button._aj1-')
        save_info.click()
        sleep(3)
        allow_notification = self.driver.find_element(By.CSS_SELECTOR, '._a9-z button._a9_1')
        allow_notification.click()
        sleep(3)

    def find_followers(self):
        # self.driver.get(URL_IG+TARGET_ACCOUNT)
        # sleep(3)
        # followers = self.driver.find_element(By.LINK_TEXT, ' followers')
        # followers.click()
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/followers")
        sleep(2)

        # model = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_bm"]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]')
        # scr1 = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas')
        # # sleep(2)
        # for i in range(5):
        #     # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model)
        #     scr1.send_keys(Keys.PAGE_DOWN)
        #     sleep(1)

    def follower(self):
        try:
            list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            for item in list_of_followers:
                print(item.text)
                if item.text == "Follow":
                    print("click")
                    item.click()
                    sleep(random.randint(1, 3))

        except Exception as e:
            print(e)

        #reference answer:
        # all_buttons = self.driver.find_elements_by_css_selector("li button")
        # for button in all_buttons:
        #     try:
        #         button.click()
        #         time.sleep(1)
        #     except ElementClickInterceptedException:
        #         cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        #         cancel_button.click()

instafollower = InstaFollower()
instafollower.login()
instafollower.find_followers()
instafollower.follower()

# instafollower.driver.quit()
