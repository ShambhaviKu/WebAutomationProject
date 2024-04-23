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

    make_appointment_btn_element = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")  #  # is denoted ID
    appointmmet_button_list = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-dark.btn-lg")  #  . is denoted Class and space


    # XPATH to CSS converter
    # //header[@id='top']/div  -- header#top > div


  #awesomqa.com/css >> CSS_SELECTOR

  # <div class="first">
  # <span>Span 1!</span>
  # <span>Span 2</span>
  # <span>Span 3!</span>
  # <span>Span 4</span>
  # <span>Span 5!</span>
  # <span>Span 6</span>
  # <span>Span 7!</span>
  # </div>

  #div.first>span:nth-child(1)
  #div.first>span:nth-child(2n+1) >> odd numbers
  #div.first>span:nth-child(2n) >>  even numbers
  #div.first>span:first-child  >> first child
  #div.first>span:last-child  >> last child