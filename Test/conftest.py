import pytest
from selenium import webdriver
from Demo.Pages.login_page import Loginpage
@pytest.fixture()
def setup():
        driver = webdriver.Firefox()
        driver.maximize_window()
