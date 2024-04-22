import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

@pytest.mark.smoke
@allure.title("Verify login")
@allure.testcase("#TC1 Verify Login")
def test_vwoLogin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()

    time.sleep(5)

    # Find element by XPATH

    # <
    # input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"  # Custom Attribute
    # >

    # login_username = driver.find_element(By.XPATH, "//input[@id='login-username']")
    login_username = driver.find_element(By.XPATH, "//input[data-qa='hocewoqisi']")
    login_username.send_keys('admin')

    allure.attach(driver.get_screenshot_as_png(), name='login-screenshot', attachment_type=AttachmentType.PNG)

    time.sleep(5)

    driver.quit()


