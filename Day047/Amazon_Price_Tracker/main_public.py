# camelcamelcamel.com
# https://www.amazon.fr/gp/product/B09V1CZ6Y8/ref=ox_sc_saved_image_9?smid=A3KN8I3OSWH3RO&psc=1
# https://myhttpheader.com
# https://python.plainenglish.io/how-to-collect-amazon-com-data-using-python-a30d3ea33fda

URL = "https://www.amazon.fr/Vangoa-Électronique-Bluetooth-Lumineuses-Rechargeable/dp/B09V1CZ6Y8/?_encoding=UTF8&pd_rd_w=0vkf6&content-id=amzn1.sym.8af26fd0-acff-4d5b-aa56-ded064cc32bd&pf_rd_p=8af26fd0-acff-4d5b-aa56-ded064cc32bd&pf_rd_r=Q07901T4FTD3MNKWACNS&pd_rd_wg=EkUfq&pd_rd_r=963e29b2-e939-4879-8233-6bf56396f2c3&ref_=pd_gw_ci_mcx_mr_hp_atf_m"


EMAIL = "from_email"
PASSWORD = "app_password"
TO_EMAIL = "to_email"
TARGET_PRICE = 200

from bs4 import BeautifulSoup
import cloudscraper
import smtplib

scraper = cloudscraper.create_scraper()
amazon_page = scraper.get(URL)
soup = BeautifulSoup(amazon_page.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText()
price_as_float = float(price.replace("€", "").replace(",", "."))
print(price_as_float)

title = soup.find(name="span", id="productTitle").getText().strip().replace("b'", "")
contents = f"{title} is now €{price_as_float}."

if price_as_float <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert! \n\n{contents}\n{URL}".encode("utf-8")
        )