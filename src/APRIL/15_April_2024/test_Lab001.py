import pytest
import time

from selenium import webdriver
import allure


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    driver.maximize_window()

    print(driver.title)

    driver.refresh()
    time.sleep(5)

    driver.forward()
    time.sleep(5)

    driver.back()
    time.sleep(5)

    driver.close()
