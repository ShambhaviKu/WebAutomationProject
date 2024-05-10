import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_relative_locators():
    driver = webdriver.Chrome()
    driver.get("https://www.awesomeqa.com/practice.html")

    # Relative Locators( Selenium 4)
    # POM, PF
    # Framework  -> BDD(behave) + Exception

    # Xpath Axes - Relatives or Siblings by using that mechanism.
    # Following sib, parent, child.

    driver.find_element(
        locate_with(By.ID, "exp-2").to_right_of({By.XPATH: "//span[text()='Years of Experience']"})).click()

    time.sleep(10)
    driver.quit()

