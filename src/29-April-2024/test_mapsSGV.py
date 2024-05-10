import pytest
import time
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


def test_mapssvg():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    time.sleep(5)

    states = driver.find_elements(By.XPATH, "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in states:
        if 'Maharashtra' in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name='state_select_screenshot', attachment_type=AttachmentType.PNG)

    driver.quit()















