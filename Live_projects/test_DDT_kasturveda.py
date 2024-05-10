import allure
import openpyxl
import pytest
import time
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
from selenium.webdriver import ActionChains
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


file_path_from_os = os.getcwd() + "/DDT_kasturveda.xlsx"
print(file_path_from_os)


@pytest.mark.parametrize("user_cred", read_credentials_from_Excel(file_path_from_os))
@allure.title("TC#1 Verify multiple login by using data driver testing")
@allure.description("Verify invalid login >> reading data from excel")
def test_kasturveda_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    kasturveda_DDT(username, password)


def kasturveda_DDT(username, password):
    driver = webdriver.Chrome()
    driver.get("https://kasturveda.com/")
    driver.maximize_window()

    time.sleep(3)

    login_dropdown = driver.find_element(By.XPATH, "//div[@class='dropdown ms-4 ms-md-0']/a/img")
    login_dropdown.click()

    time.sleep(3)

    login = driver.find_element(By.LINK_TEXT, "Log In")
    login.click()

    username_input = driver.find_element(By.ID, "email")
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    time.sleep(10)

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

    actions = ActionChains(driver)
    actions.move_to_element(login_btn).click().perform()

    time.sleep(5)

    result = driver.current_url  # Negative TC using Invalid Dta
    if result == "https://kasturveda.com/login":
        ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=ignore_list)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='pl-3 mb-0 list-inline']/li"))
        )

        error_msg = driver.find_element(By.XPATH, "//ul[@class='pl-3 mb-0 list-inline']/li")
        assert error_msg.text == "These credentials do not match our records."
        print(error_msg.text)
        allure.attach(driver.get_screenshot_as_png(), name="InValidData_screenshot", attachment_type=AttachmentType.PNG)

    else:  # positive test case

        wait = WebDriverWait(driver, 30)
        wait.until(
            EC.text_to_be_present_in_element((By.XPATH, "(//a[@href='https://kasturveda.com/about-us'])[1]"),
                                             'About kasturveda')
        )

        page_heading = driver.find_element(By.XPATH, "(//a[@href='https://kasturveda.com/about-us'])[1]")
        assert page_heading.text == "About kasturveda"

        allure.attach(driver.get_screenshot_as_png(), name="ValidData_screenshot", attachment_type=AttachmentType.PNG)

    driver.quit()
