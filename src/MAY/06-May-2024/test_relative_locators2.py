import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_relative_locators():
    driver = webdriver.Chrome()
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")
    time.sleep(5)

    search_city = driver.find_element(By.XPATH, "//input[@id='search_city']")
    search_city.send_keys("India")
    time.sleep(10)

    states = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")


    for state in states:
        if "India" in state.text:
            s1 = driver.find_element(locate_with(By.TAG_NAME, "p").to_right_of(state)).text
            s2 = driver.find_element(locate_with(By.TAG_NAME, "p").to_left_of(state)).text
            s3 = driver.find_element(locate_with(By.TAG_NAME, "p").above(state)).text
            s4 = driver.find_element(locate_with(By.TAG_NAME, "p").below(state)).text

            print(s1 + "|" + state.text + "|" + s2)
            print(s3 + "|" + state.text + "|" + s4)

    driver.quit()
