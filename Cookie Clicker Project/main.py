from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 60 * 5

while True:
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()
    if time.time() % 5 < 0.1:
        store_items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        cookie_count = driver.find_element(By.ID, "money").text.replace(",", "")
        if cookie_count.isdigit():
            cookies = int(cookie_count)
            for item in reversed(store_items):
                if item.text:
                    name_price = item.text.split("-")
                    if len(name_price) > 1:
                        item_price = int(name_price[1].strip().replace(",", ""))
                        if cookies >= item_price:
                            print(f"Buying {name_price[0].strip()} for {item_price} cookies.")
                            item.click()
                            break
    if time.time() > timeout:
        print("Time limit reached!")
        cookie_per_second = driver.find_element(By.ID, value="cps").text
        print(f"Final Cookies per Second: {cookie_per_second}")
        break
    time.sleep(0.1)