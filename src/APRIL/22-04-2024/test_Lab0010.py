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
    last_name = driver.find_element(By.NAME, "lastname")

    action = ActionChains(driver)

    action \
        .move_to_element(first_name) \
        .key_down(Keys.SHIFT) \
        .send_keys_to_element(first_name, "shambhavi").key_up(Keys.SHIFT).perform()

    action \
        .key_down(Keys.CONTROL) \
        .send_keys('a') \
        .key_down(Keys.CONTROL) \
        .send_keys('c') \
        .move_to_element(last_name) \
        .click(last_name) \
        .key_down(Keys.CONTROL) \
        .send_keys('v').perform()

    radio_female = driver.find_element(By.CSS_SELECTOR, " #sex-1")
    radio_female.click()

    radio_exp = driver.find_element(By.CSS_SELECTOR, "#exp-1")
    radio_exp.click()

    date = driver.find_element(By.ID, 'datepicker')
    action.move_to_element(date).click_and_hold(date).send_keys_to_element(date, "06-12-1994").perform()

    profession1 = driver.find_element(By.ID, 'profession-0')
    profession1.click()

    profession2 = driver.find_element(By.ID, 'profession-1')
    profession2.click()

    tools1 = driver.find_element(By.ID, "tool-0")
    tools1.click()

    tools2 = driver.find_element(By.ID, "tool-2")
    tools2.click()

    continents = driver.find_elements(By.TAG_NAME, 'option')
    # continents[1].click()

    i = 0
    while i < len(continents):
        if continents[i].text == 'Africa':
            continents[i].click()
        i = i + 1

    time.sleep(15)
