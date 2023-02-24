#pip3 install -U selenium
#pip3 install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="../Development")

driver = webdriver.Chrome(options=options, service=service)

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.fr/Vangoa-Électronique-Bluetooth-Lumineuses-Rechargeable/dp/B09V1CZ6Y8/?_encoding=UTF8&pd_rd_w=0vkf6&content-id=amzn1.sym.8af26fd0-acff-4d5b-aa56-ded064cc32bd&pf_rd_p=8af26fd0-acff-4d5b-aa56-ded064cc32bd&pf_rd_r=Q07901T4FTD3MNKWACNS&pd_rd_wg=EkUfq&pd_rd_r=963e29b2-e939-4879-8233-6bf56396f2c3&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
price = driver.find_element(By.CLASS_NAME, 'a-price-whole')  #get_attribute, get_tagName, webForm, size, by_css_elements (".class tag"), driver.find_element by xpath('...')
print(price.text)



# driver.close()
driver.quit()

