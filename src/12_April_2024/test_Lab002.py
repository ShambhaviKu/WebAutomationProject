from selenium import webdriver
import time

def test_loginVWO():
    Driver = webdriver.Chrome()  # Create the session -- POST Request
    Driver.get("https://app.vwo.com/")  # GET Request to url param
    Driver.maximize_window()

    time.sleep(5)
