URL_IG = "https://instagram.com"

SIMILAR_ACCOUNT = "annabel_zheng"
IG_ID = "komfeecoing"
IG_PASSWORD = "23Engineer@nna"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException


class InstaFollower:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.service = Service(executable_path="../Development")
        self.driver = webdriver.Chrome(options=self.options, service=self.service)

    def login(self):
        self.driver.get(URL_IG)
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js-start-test span.start-text').click()
        sleep(40)

        while True:
            try:
                self.driver.find_element(By.LINK_TEXT, 'Back to test results').click()
                break
            except ElementNotInteractableException:
                pass
            except StaleElementReferenceException:
                pass

        self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)


    def find_followers(self):
        pass

    def follower(self):
        pass

instafollower = InstaFollower()
instafollower.login()
instafollower.find_followers()
instafollower.follower()


#     def tweet_at_provider(self):
#         self.driver.get(URL_TWITTER)
#         sleep(5)
#         self.driver.find_element(By.CSS_SELECTOR, '.css-1dbjc4n a').click()
#         sleep(5)
#         input_email = self.driver.find_element(By.NAME, 'text')
#         input_email.send_keys(TWITTER_EMAIL)
#         input_email.send_keys(Keys.ENTER)
#         sleep(5)
#         # Retype for security reason
#         input_user = self.driver.find_element(By.NAME, 'text')
#         input_user.send_keys(TWITTER_USER)
#         input_user.send_keys(Keys.ENTER)
#         sleep(5)
#         input_pw = self.driver.find_element(By.NAME, 'password')
#         input_pw.send_keys(TWITTER_PASSWORD)
#         input_pw.send_keys(Keys.ENTER)
#         sleep(5)
#
#         simple_tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 150down/10up? "
#
#         input_twitter = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
#         input_twitter.send_keys(simple_tweet)
#         sleep(3)
#
#         ## CAPTCHA shows here for security, didn't get to test the following codes.
#         maybe_share_later = self.driver.find_element(By.XPATH,
#                                                      '//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[4]')
#         maybe_share_later.click()
#
#         tweet_button = self.driver.find_element(By.XPATH,
#                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
#         tweet_button.click()
#
#         sleep(5)
#
#
# bot = InternetSpeedTwitterBot()
# internet_speed = internetSpeedTwitterBot.get_internet_speed()
# print(f"Download Speed: {bot.down}")
# print(f"Upload Speed: {bot.up}")
#
# if bot.up < PROMISED_DOWN or bot.down < PROMISED_UP:
#     bot.tweet_at_provider()

bot.driver.quit()
