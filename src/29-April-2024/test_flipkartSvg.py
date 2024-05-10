import pytest
import time
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)

def test_flipkartsvg():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    time.sleep(3)

    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys("AC")

    search_icon = driver.find_elements(By.XPATH, "//*[name()='svg']")
    search_icon[0].click()

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="Login_screenshot", attachment_type=AttachmentType.PNG)