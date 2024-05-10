import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *

def test_google():
    driver = webdriver.Chrome()
    driver.get('https://www.google.co.in/')

    try:
        driver.find_element(By.NAME, "shambhavi").send_keys("the testing academy")
    except NoSuchElementException as NCC:
        print(f"No such element found and loactor {NCC}")\

    time.sleep(10)
    driver.quit()
