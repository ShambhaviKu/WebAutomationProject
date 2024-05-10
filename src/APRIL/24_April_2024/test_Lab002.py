import pytest
import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


def test_vwoLogin_negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()



    #driver.implicitly_wait(5)


    username_element = driver.find_element(By.NAME, "username")
    username_element.send_keys("admin")


    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys("admin@123")

    signin_element = driver.find_element(By.ID, "js-login-btn")
    signin_element.click()

    #Fluent wait

    exception_list = [ElementNotVisibleException, ElementNotSelectableException]

    wait = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=exception_list)
    wait.until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
    )

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)

    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()
