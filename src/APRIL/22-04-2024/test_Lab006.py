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
    hoverable = driver.find_element(By.XPATH, "//input[@id='hover']")

    actions = ActionChains(driver)

    actions.move_to_element(hoverable).perform()

    draggable = driver.find_element(By.ID, 'draggable')
    droppable = driver.find_element(By.ID, 'droppable')

    actions.drag_and_drop(draggable, droppable).perform()

    time.sleep(5)






