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

    time.sleep(10)

    username_element = driver.find_element(By.NAME, 'username')
    username_element.send_keys('Admin')

    password_element = driver.find_element(By.NAME, 'password')
    password_element.send_keys('admin123')

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit'] ")
    login_btn.click()

    time.sleep(5)

    user_role = driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
    user_role[0].click()

    time.sleep(5)

    user_role_list = driver.find_elements(By.XPATH, "//div[@data-v-d130bb63=""]")

    i = 0
    while i < len(user_role_list):
        if user_role_list[i].text == 'Admin':
            user_role_list[i].click()
            break
        else:
            i = i + 1

    emp_name = driver.find_element(By.XPATH, "//input[@data-v-75e744cd=""]")
    emp_name.send_keys('a')

    time.sleep(5)

    username = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")
    username.send_keys('Test_user')

    password = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
    password.send_keys('Test@123')

    cofirm_paaword = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
    cofirm_paaword.send_keys("Test@123")

   # user_details[2].send_keys("test_user")

   # user_details[4].send_keys("Test@123")

    time.sleep(10)


