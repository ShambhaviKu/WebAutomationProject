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
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


def test_frame():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    actions = ActionChains(driver)

    iframe = driver.find_element(By.TAG_NAME, 'iframe')

    #actions.scroll_to_element(iframe).perform()

    scroll_origin = ScrollOrigin.from_element(iframe)

    actions.scroll_from_origin(scroll_origin, 0, 200).perform()

    time.sleep(50)

