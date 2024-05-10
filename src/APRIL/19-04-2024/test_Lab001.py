import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify login in cura katalon website")
@allure.testcase("Verify simple login in cura katalon website ")
def test_katalon_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # find element by Link Text
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg"
    # >Make Appointment                    -- Link Text
    # </a>

    # make_appointment_button = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # make_appointment_button.click()

    # Find element by partial link text

    # make_appointment_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    # make_appointment_button.click()

    # Find element bt TAG NAME
    make_appointment_button = driver.find_elements(By.TAG_NAME, 'a')
    make_appointment_button[5].click()

    allure.attach(driver.get_screenshot_as_png(), name="Login-screenshot", attachment_type=AttachmentType.PNG)

    # check current url
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Assertion fail message #TC1 = Error matching URLs"

    username_element = driver.find_element(By.ID, "txt-username")
    username_element.send_keys("John Doe")

    password_element = driver.find_element(By.ID, "txt-password")
    password_element.send_keys("ThisIsNotAPassword")

    login_element = driver.find_element(By.ID, "btn-login")
    login_element.click()

    allure.attach(driver.get_screenshot_as_png(), name="Appointment-screenshot", attachment_type=AttachmentType.PNG)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Assertion fail mesaage #TC2 = Error matching URLs"

    time.sleep(5)

    driver.quit()

