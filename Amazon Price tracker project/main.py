import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://www.amazon.com/100-Pure-European-Linen-Sheet/dp/B0D9L138Z5/ref=sr_1_2_sspa?_encoding=UTF8&content-id=amzn1.sym.83009b1f-702c-4be7-814b-0240b8f687d2&dib=eyJ2IjoiMSJ9.hHtb-dXMvILCfpeNlrQZ2HBaF5Reo4aF1ozN_YfBKS5vH7g2ZgWsfv8GfcRwzMjXLglxBVKPDA7seS4yoz90igjAF4Blj4DYd1pArInd7QNRilc3NK58tIPvjIKZp3_YmillotvyQsVMOtNEEXyMbmNew5OTWXZrDDoSlcANYO4A-YydYbBxn6Hezh2lpKXuVSzP62oGlGJmPt_aTtNj_59tUBiR93nzTPv15EV5nWAAVnWezIeqdHWV5XyPRCRIs0-fhAuOZGqVPCfgbXo0011k3dpaFtMl2ZeeY5GCk14.CsTPbGiYYq3sVAsBCQBdo9Job1H-VRuBQu4Az43BOfg&dib_tag=se&keywords=bedding&pd_rd_r=74e48142-3935-481e-956c-d2298975ef10&pd_rd_w=4WfGu&pd_rd_wg=vh18v&qid=1738681573&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
response = requests.get(URL, headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Opera GX\";v=\"116\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0",
  })
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
print(soup.prettify())
price = soup.find(class_="aok-offscreen").getText()
price_split = price.split("$")[1]
price_as_float = float(price_split)

product_name = soup.find(id="productTitle").getText().strip()

target_price = 120
if price_as_float < target_price:
    message = f"{product_name} is now for ${price_as_float}"

    my_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    with smtplib.SMTP(os.getenv("SMTP_ADDRESS")) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mirzaskilful@gmail.com",
            msg=f"Subject: Amazon Price Alert \n\n {message}".encode("utf-8")
        )