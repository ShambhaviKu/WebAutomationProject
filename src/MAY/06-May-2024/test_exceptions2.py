import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *

def test_google():
    driver = webdriver.Chrome()
    driver.get('https://www.google.co.in/')
    driver.maximize_window()

    try:
        google_search = driver.find_element(By.NAME, "q")
        driver.refresh()
        time.sleep(5)

        # google_search = driver.find_element(By.NAME, "q")
        google_search.send_keys("the testing academy")
    except StaleElementReferenceException as SEE:
        print(SEE)

    time.sleep(10)
    driver.quit()
