import allure
import openpyxl
import pytest
import time
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os


def read_credentials_from_Excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({
            "username": username,
            "password": password
        })
    return credentials


file_path_from_os = os.getcwd() + "/DDT_webAutomation.xlsx"
print(file_path_from_os)


@pytest.mark.parametrize("user_cred", read_credentials_from_Excel(file_path_from_os))
@allure.title("TC#1 Verify multiple login by using data driver testing")
@allure.description("Verify invalid login >> reading data from excel")
def test_Vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    vwo_DDT(username, password)


def vwo_DDT(username, password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    username_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    username_input.send_keys(username)

    password_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    password_input.send_keys(password)

    time.sleep(5)

    submit_btn = driver.find_element(By.ID, "js-login-btn")
    submit_btn.click()

    time.sleep(5)

    result = driver.current_url  # Negative TC using Invalid Dta
    if result != "https://app.vwo.com/#/dashboard":
        ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

        wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=ignore_list)
        wait.until(
            EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
        )

        error_msg = driver.find_element(By.ID, "js-notification-box-msg")
        assert error_msg.text == "Your email, password, IP address or location did not match"
        print(error_msg.text)
        allure.attach(driver.get_screenshot_as_png(), name="InValidData_screenshot", attachment_type=AttachmentType.PNG)

    else:     # positive test case
        wait = WebDriverWait(driver, 30)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), 'Dashboard')
        )

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-qa='lufexuloga']")))

        page_heading = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
        assert page_heading.text == "Shambhavi test"

        allure.attach(driver.get_screenshot_as_png(), name="ValidData_screenshot", attachment_type=AttachmentType.PNG)

    driver.quit()
