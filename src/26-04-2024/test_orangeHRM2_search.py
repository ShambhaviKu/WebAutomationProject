import pytest
import time
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


def test_user_ops():
    driver = webdriver.Edge()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")
    driver.maximize_window()

    time.sleep(10)

    username_element = driver.find_element(By.NAME, 'username')
    username_element.send_keys('Admin')

    password_element = driver.find_element(By.NAME, 'password')
    password_element.send_keys('admin123')

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit'] ")
    login_btn.click()

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="login_screenshot", attachment_type=AttachmentType.PNG)


    # user role
    user_roles = driver.find_elements(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])")
    user_roles[0].click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@role='listbox']//div)[2]").click()
    time.sleep(2)

    # Employee name
    emp_name = driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']")
    emp_name.send_keys('a')
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@role='listbox']/div)[5]").click()

    # status
    status_element = driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
    status_element[1].click()
    status_element = driver.find_element(By.XPATH,"(//div[@role='option'])[2]")
    status_element.click()
    time.sleep(5)

    # username
    username = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'][@autocomplete='off'])[1]")
    username.send_keys("Automation")

    # password
    password = driver.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active'][@type='password'][@autocomplete='off']")
    password[0].send_keys("Tester@123")
    password[1].send_keys("Tester@123")

    # save button
    save = driver.find_element(By.XPATH, "//button[@type='submit']")
    save.click()

    allure.attach(driver.get_screenshot_as_png(), name="UserCreation_screenshot", attachment_type=AttachmentType.PNG)


    time.sleep(10)

    # search user

    actions = ActionChains(driver)
    search_user = driver.find_elements(By.XPATH, "(//input[@data-v-1f99f73c=''])")

    actions.move_to_element(search_user[1]).click(search_user[1]).send_keys("Automation").perform()

    search_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_btn.click()

    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name="search_screenshot", attachment_type=AttachmentType.PNG)

    search_result = driver.find_element(By.XPATH, "(//div[@data-v-6c07a142=''])[1]")
    assert search_result.text == "Automation"



    time.sleep(10)





