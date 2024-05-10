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
@allure.title("Positive test case")
@allure.description("verify dashboard after succesful login ")
def test_vwoLogin_positive():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()

    # driver.implicitly_wait(5)

    username_element = driver.find_element(By.NAME, "username")
    username_element.send_keys("shambhavi@gmail.com")

    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys("Testing@123")

    signin_element = driver.find_element(By.ID, "js-login-btn")
    signin_element.click()

    # Fluent wait

    exception_list = [ElementNotVisibleException, ElementNotSelectableException]

    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=exception_list)
    wait.until(
        EC.text_to_be_present_in_element(((By.CLASS_NAME, "page-heading")), 'Dashboard')
    )

    page_title = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    assert page_title.text == 'Shambhavi test'

    allure.attach(driver.get_screenshot_as_png(), name='scrennshot', attachment_type=AttachmentType.PNG)

    driver.quit()
