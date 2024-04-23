import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


def test_ebay_function():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.maximize_window()
    time.sleep(5)

    search_element = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_element.send_keys("16gb")

    search_btn_element = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_btn_element.click()

    allure.attach(driver.get_screenshot_as_png(), name="Screnshot", attachment_type= AttachmentType)

    list_of_elements = driver.find_elements(By.XPATH, "//span[@role='heading']")

    for product in list_of_elements:
        product_name = product.text
        print(product_name)

    product_price_element_list = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    prize = []
    for price in product_price_element_list:
        product_price = price.text
        print(product_price)
        x = product_price.replace("$", " ").strip()
        prize.append(x)

    prize.sort()
    #min_price = prize[1]
    print(f"cheapest price is {prize[1]}")

    time.sleep(5)
