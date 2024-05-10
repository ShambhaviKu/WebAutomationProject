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
@allure.title("Verify registration")
@allure.description("Verify successfull registration")
@allure.testcase("TC#1 Registration")
def test_kasturveda_reg_positive():
    driver = webdriver.Chrome()
    driver.get("https://kasturveda.com/")

    time.sleep(5)
    driver.maximize_window()

    time.sleep(3)

    signup = driver.find_element(By.XPATH, "//div[@class='dropdown ms-4 ms-md-0']/a/img")
    signup.click()

    time.sleep(2)

    reg = driver.find_element(By.LINK_TEXT, 'Create Account')
    reg.click()
    time.sleep(5)

    first_name = driver.find_element(By.ID, "txtOnly1")
    first_name.send_keys('shambhavi')

    last_name = driver.find_element(By.ID, "txtOnly2")
    last_name.send_keys('Kulkarni')

    email = driver.find_element(By.ID, "email")
    email.send_keys("hpxaemkrf3@gmail.com")

    number = driver.find_element(By.ID, "contact_no")
    number.send_keys('8965231256')

    password = driver.find_element(By.ID, "password")
    password.send_keys("Kulkarni@123")

    btn = driver.find_element(By.XPATH, "//button[@id='btn_signup']")
    btn.click()

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name = "registration_screenshot", attachment_type=AttachmentType.PNG)