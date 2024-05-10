import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.awesomeqa.com/practice.html")
    driver.maximize_window()

    first_name = driver.find_element(By.NAME, "firstname")

    action = ActionChains(driver)
    action.key_down(Keys.SHIFT).send_keys_to_element(first_name, "the testing academy").key_up(Keys.SHIFT).perform()

    download = driver.find_element(By.XPATH, "//a[contains(text(), 'Click here')]")
    action.context_click(download).perform()

    time.sleep(5)



