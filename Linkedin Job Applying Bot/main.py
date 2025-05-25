from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
try:
    cancel = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/button'))
    )
    cancel.click()
except:
    print("Cancel button not found or already closed")

sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()
email = driver.find_element(By.NAME, value="session_key")
email.send_keys("#Your Email")

password = driver.find_element(By.ID, value="password")
password.send_keys("#Your Password")
try:
    sign_in_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[4]/button')
    sign_in_button.click()
except:
    print("Cannot find Sign in Button!")

save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "job-card-list"))
)
while True:
    jobs = driver.find_elements(By.CLASS_NAME, value="job-card-list")
    if not jobs:
        print("No Jobs Found")
    for job in jobs:
        job.click()
        time.sleep(2)

        save_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "jobs-save-button"))
        )
        save_button.click()
        print("Job saved successfully!")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)