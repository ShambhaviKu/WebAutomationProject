import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify login in cura katalon website")
@allure.testcase("Verify simple login in cura katalon website ")
def test_katalon_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # * find element from all tags >> it takes time

    # make_appointment_btn_element = driver.find_element(By.XPATH, "//*[@id='btn-make-appointment']")


    # XPATH using link text

    # make_appointment_btn_element = driver.find_element(By.XPATH, "//a[text()='Make Appointment']")

    # XPATH using partial link text
    # // a[contains(text(), 'Make Appointment')]
    # // a[contains(text(), 'Make')]
    # // a[contains(text(), 'Appointment')]
    # // a[contains(text(), 'App')]  --- App will be more than one > make sure this should be unique


  # XPATH using Starts-with & ends-with

  # //a[starts-with(text(),'Make')]
  # //a[endss-with(text(),'Appointment')]

  # XPATH using and and or

  # //a[text()='Make Appointment' and contains(@id, 'btn') and @class="btn btn-dark btn-lg"]
  # //a[text()='Make Appointment' or contains(@id, 'btn') and @class="btn btn-dark btn-lg"]




