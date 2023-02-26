
#FIRST URL applied the first job
#US
#URL = "https://www.linkedin.com/jobs/search/?currentJobId=3494424397&f_AL=true&f_E=2&f_TPR=r604800&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&refresh=true"
#UK
#URL = "https://www.linkedin.com/jobs/search/?currentJobId=3498743191&f_AL=true&f_E=2&f_TPR=r604800&f_WT=2&geoId=101165590&keywords=python%20developer&location=United%20Kingdom&refresh=true"
#EUROPE
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3364415815&f_AL=true&f_E=2&f_WT=2&geoId=100506914&keywords=python%20developer&location=Europe&refresh=true"
ACCOUNT_ID = "id"
ACCOUNT_PW = "password"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="../Development")
driver = webdriver.Chrome(options=options, service=service)
driver.get(URL)

# sign_in = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in = driver.find_element(By.CSS_SELECTOR, 'div.nav__cta-container a.nav__button-secondary')
sign_in.click()
# privacy = driver.find_element(By.CSS_SELECTOR, 'section.artdeco-global-alert__body .artdeco-button--2')
# privacy.click()

time.sleep(1)

# sign in
input_id = driver.find_element(By.ID, 'username')
input_id.send_keys(ACCOUNT_ID)
input_pw = driver.find_element(By.ID, 'password')
input_pw.send_keys(ACCOUNT_PW)
# input_pw.send_keys(Keys.ENTER)
sign_in_action = driver.find_element(By.CSS_SELECTOR, "button.from__button--floating")
sign_in_action.click()

time.sleep(1)

# result_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

# for job_list in result_list:
#     if "python" in job_list.text.lower():
#         print(f"Call {job_list.text}")
#         job_list.click()
#         driver.find_element(By.CLASS_NAME, "jobs-save-button").click()

# jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item") #TO APPLY
# jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list") #TO SAVE
jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

# store current window (browser tab) id, that will help us in final step, wait for that.
main_window_id = driver.current_window_handle
i = 1
j = 1
job_list = []

for job in jobs_list:
    print(job.text)
    job_list.append(job.text)
    print(j)

    # click on single job from jobs list using loop
    job_des = job_list[j-1].lower()

    if "python" in job_des:
        job.click()
        # print(f"Call {job.text}")
        # print("job click ", i)
        i += 1
        time.sleep(2)

        driver.find_element(By.CLASS_NAME, "jobs-save-button").click()

    j += 1

        # Apply for the job
        # try:
        #     driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()
        #     driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click() #Confirm Info
        #     driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div[1]/div/div[2]/div/div[2]/button[1]").click() #CHOOSE
        #     time.sleep(2)
        #     driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click() #CONFIRM RESUME
        #     driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click() #SAVE APPLICATION
        #     driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click() #CONFIRM EDUCATION
        #     driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click() #REVIEW
        #     # driver.find_element(By.ID, "follow-company-checkbox").click() #unfollow company
        #     driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click() #SUBMIT
        #     time.sleep(2)
        #     break
        # except NoSuchElementException:
        #     print("No application button, skipped.")
        #     break

