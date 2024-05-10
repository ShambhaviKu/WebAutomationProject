import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_task07():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.maximize_window()

    driver.switch_to.frame(driver.find_element(By.ID, "result"))

    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()

    # username = driver.find_element(By.XPATH, "//input[@id='username']")
    error_message = driver.find_element(
        locate_with(By.XPATH, "//small[text()='Username must be at least 3 characters']").below({By.XPATH: "//input[@id='username']"}))

    print(error_message.text)
    assert error_message.text == "Username must be at least 3 characters"

    time.sleep(10)
    driver.quit()


