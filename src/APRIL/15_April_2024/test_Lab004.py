import pytest
import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


def test_vwoLogin_negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()

    time.sleep(5)

    # Find an element

    # <input type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi">

    username_element = driver.find_element(By.NAME, "username")
    username_element.send_keys("admin")

    # <input type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # aria-autocomplete="list">
    password_element = ""

    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys("admin@123")

    #<button type="submit"
    # id="js-login-btn" class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica"> <span class="icon loader hidden" data-qa="zuyezasugu"></span>

    signin_element = driver.find_element(By.ID, "js-login-btn")
    signin_element.click()

    time.sleep(5)

    # <div class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email, password,
    # IP address or location did not match</div>

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)

    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()
