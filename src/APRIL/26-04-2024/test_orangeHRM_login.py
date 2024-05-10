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

@pytest.mark.smoke
@allure.title("PositiveTC#1 Login")
@allure.description("Verify successfull Login")
def test_login_positive():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(5)

    username_element = driver.find_element(By.NAME,'username')
    username_element.send_keys('Admin')

    password_element = driver.find_element(By.NAME, 'password')
    password_element.send_keys('admin123')

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit'] ")
    login_btn.click()

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name='Login_screenshot', attachment_type=AttachmentType.PNG)

    driver.quit()


