import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


def test_table_ops():
    driver = webdriver.Chrome()
    driver.get("https://www.awesomeqa.com/webtable.html")

    time.sleep(5)

    # row element
    row_element = driver.find_elements(By.XPATH, "//table[contains(@id, 'cust')]/tbody/tr")
    row = len(row_element)
    print(row)

    time.sleep(5)

    # colums_element
    cols_element = driver.find_elements(By.XPATH, "//table[contains(@id, 'cust')]/tbody/tr[2]/td")
    col = len(cols_element)
    print(col)

    time.sleep(5)

    # //table [contains(@id, 'cust')]/tbody/tr[
    # 2 >> i
    # ]/td
    # [
    # 1 >> j
    # ]

    first_part = "//table [contains(@id, 'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country = driver.find_element(By.XPATH, country_path).text
                print(country)

    time.sleep(5)
