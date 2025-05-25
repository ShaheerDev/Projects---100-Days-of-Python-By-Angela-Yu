from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")
# num_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# # num_of_articles.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Shaheer")

lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Mirza")

email = driver.find_element(By.NAME, value="email")
email.send_keys("mirzaskilful@gmail.com", Keys.ENTER)