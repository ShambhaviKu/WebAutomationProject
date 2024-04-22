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
def test_iDriveLogin():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()

    # <
    # input
    # _ngcontent-ytb-c4="" autofocus=""
    # class="id-form-ctrl ng-pristine ng-valid ng-touched"
    # id="username"
    # name="username"
    # type="email"
    # >

    # Find element by XPATH

    login_username = driver.find_element(By.XPATH, "//input[@id='username']")
    login_username.send_keys("augtest_040823@idrive.com")

    # <
    # input
    # _ngcontent-ytb-c4=""
    # class="id-form-ctrl ng-untouched ng-pristine ng-valid"
    # id="password"
    # name="password" tabindex="0"
    # type="password"
    # >

    login_password = driver.find_element(By.XPATH, "//input[@id='password']")
    login_password.send_keys('123456')

    # <button
    # _ngcontent-xio-c4="" class="id-btn id-info-btn-frm"
    # id="frm-btn"
    # type="submit"
    # >Sign in</button>

    signin_button = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    signin_button.click()

    time.sleep(25)

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "!assert error = url not mtched"

    # <h5
    # _ngcontent-wbe-c10=""  -- custom Attribute
    # class="id-card-title"
    # >Your free trial has expired<
    # /h5>

    text_element = driver.find_element(By.XPATH, "//h5[@class='id-card-title']")
    assert text_element.text == "Your free trial has expired"

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)

    driver.quit()
