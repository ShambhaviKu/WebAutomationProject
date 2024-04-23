import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify error message")
@allure.testcase("Verify error massage has come after clicking on the submit button ")
def test_reg_Negative():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(3)

    driver.switch_to.frame(driver.find_element(By.ID, "result"))

    email_element = driver.find_element(By.XPATH, "//input[@id='email']")
    email_element.send_keys("shambhavikulkarni@gmail.com")

    password_element = driver.find_element(By.XPATH, "//input[@id='password']")
    password_element.send_keys("123123")

    password2_element = driver.find_element(By.XPATH, "//input[@id='password2']")
    password2_element.send_keys("123123")

    submit_btn_element = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    submit_btn_element.click()

    time.sleep(2)

    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType)

    error_msg_element = driver.find_element(By.XPATH, "//div[@class='form-control error']/small")
    assert error_msg_element.text == "Username must be at least 3 characters"

    time.sleep(3)
