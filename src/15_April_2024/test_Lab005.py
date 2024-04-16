import pytest
import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


def test_task1():
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

    time.sleep(5)

    # <input type="text" class="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value="" autocomplete="off">

    username_element = driver.find_element(By.ID, "txt-username")
    username_element.send_keys("John Doe")

    password_element = driver.find_element(By.ID, "txt-password")
    password_element.send_keys("ThisIsNotAPassword")

    # <button
    # id="btn-login"
    # type="submit"
    # class="btn btn-default">Login</
    # button>

    login_element = driver.find_element(By.ID, "btn-login")
    login_element.click()

    time.sleep(5)

    print(driver.current_url)


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(5)

    text_element = driver.find_element(By.XPATH, "//div/h2")
    print(text_element.text)

    assert text_element.text == "Make Appointment"
    time.sleep(5)

    driver.quit()
