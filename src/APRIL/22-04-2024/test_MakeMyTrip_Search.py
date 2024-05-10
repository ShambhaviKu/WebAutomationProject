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


def test_makemytrip():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    time.sleep(10)

    from_city_btn = driver.find_element(By.ID, "fromCity")
    from_city_btn.click()

    time.sleep(10)

    city_input = driver.find_element(By.XPATH, "//div[@class='autoSuggestPlugin hsw_autocomplePopup']/div/input")
    #city_input.send_keys('Pune')

    time.sleep(5)

    from_city_dropdown = driver.find_elements(By.XPATH, "//p[@class='font14 appendBottom5 blackText']")
    #print(from_city_dropdown[0].text)

    i = 0
    while i < len(from_city_dropdown):
        if from_city_dropdown[i].text == 'Pune, India':
            from_city_dropdown[i].click()
            break
        else:
            i = i + 1

    time.sleep(5)

    to_city_btn = driver.find_element(By.ID, "toCity")
    to_city_btn.click()

    time.sleep(5)

    to_city_dropdown = driver.find_elements(By.XPATH, "//p[@class='font14 appendBottom5 blackText']")

    i = 0
    while i < len(to_city_dropdown):
        if to_city_dropdown[i].text == 'Mumbai, India':
            to_city_dropdown[i].click()
            break
        else:
            i = i + 1

    time.sleep(10)

    for i in range(12):
        month_year = driver.find_element(By.XPATH, "//div[@class='DayPicker-Month']/div[@class='DayPicker-Caption']")
        if month_year.text == 'June 2024':
            date = driver.find_element(By.XPATH,"//div[@aria-label='Sat Jun 08 2024']")
            date.click()
            break
        else:
            btn = driver.find_element(By.XPATH, "//span[@class='DayPicker-NavButton DayPicker-NavButton--next']")
            btn.click()
            time.sleep(10)

    travellers = driver.find_element(By.XPATH,"//span[@class='lbl_input appendBottom5']")
    travellers.click()

    time.sleep(3)

    adults = driver.find_element(By.XPATH, "//li[@data-cy='adults-5']")
    adults.click()

    apply_btn = driver.find_element(By.XPATH, "//button[@data-cy='travellerApplyBtn']")
    apply_btn.click()

    time.sleep(3)

    radio_btn = driver.find_elements(By.XPATH, "//span[@class='outer']")
    radio_btn[1].click()

    #i = 0
    #while i < len(radio_btn):
        #if radio_btn[i].text == 'Student':
            #radio_btn[i].click()
            #break
        #else:
            #i = i + 1

    time.sleep(10)


    search_btn = driver.find_element(By.XPATH, "//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']")
    search_btn.click()

    time.sleep(10)
