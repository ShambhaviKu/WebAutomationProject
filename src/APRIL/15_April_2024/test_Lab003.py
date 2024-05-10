import pytest
import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


def test_loginFUnc():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    time.sleep(5)

    # Find an element

    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login
    # "class="btn btn-dark btn-lg">Make Appointment
    # </a>

    login_element = driver.find_element(By.ID, "btn-make-appointment")
    login_element.click()

    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.close()