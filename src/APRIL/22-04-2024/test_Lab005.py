import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_mouse_interactions():
    driver = webdriver.Chrome()
    driver.get("https://www.awesomeqa.com/selenium/mouse_interaction.html")
    click_btn = driver.find_element(By.XPATH, "//a[@id='click']")

    actions = ActionChains(driver)
   # actions.click_and_hold(click_btn).perform()

    #actions.click(click_btn).perform()
    #assert driver.current_url == "https://www.awesomeqa.com/selenium/resultPage.html", "assert Error=url not matching"

    click_input = driver.find_element(By.XPATH, "//input[@id='clickable']")
    actions\
        .move_to_element(click_input)\
        .click_and_hold(click_input).key_down(Keys.SHIFT)\
        .send_keys_to_element(click_input, 'shambahvi')\
        .key_up(Keys.SHIFT).perform()

    actions.click(click_btn).perform()

    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.perform()

    time.sleep(5)




