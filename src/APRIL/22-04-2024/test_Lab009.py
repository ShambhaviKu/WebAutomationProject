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

def test_window_handle():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")

    link = driver.find_element(By.LINK_TEXT, 'Click Here')
    link.click()

    parent_window = driver.current_window_handle
    print(parent_window)

    time.sleep(5)

    total_window = driver.window_handles
    print(total_window)

    for handle in total_window:
        driver.switch_to.window(handle)
        if 'New Window' in driver.page_source:
            print('Text found')
            break


