from selenium import webdriver
import time
import pytest

@pytest.mark.smoke
def test_loginVWO():
    Driver = webdriver.Chrome()  # Create the session -- POST Request
    Driver.get("https://app.vwo.com/")  # GET Request to url param
    Driver.maximize_window()

    Title = Driver.title
    print(Title)
    assert Title == "Login - VWO"

    #print(Driver.page_source)

    print(Driver.session_id)

    time.sleep(5)
