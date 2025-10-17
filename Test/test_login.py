import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from ..Pages.login_page import Loginpage
from utilities.read_properties import Read_config


class Test01AdminLogin:
    login_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    inv_username = "standard_user123"
    inv_password = "secret_sauce123"


    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.login = Loginpage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_valid_login(self):
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(10)
        self.login.enter_username(self.username)
        self.login.enter_password(self.password)
        self.login.click_login()
        self.driver.implicitly_wait(10)
        exp1_validation =self.driver.find_element(By.XPATH,"//h6[text()='Dashboard']").text
        print(f'{exp1_validation}')


    def test_login_invalid(self):
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(10)
        self.login.enter_username(self.inv_username)
        self.login.enter_password(self.inv_password)
        self.login.click_login()
        self.driver.implicitly_wait(10)
        exp_validation ="Invalid credentials"
        act_validation =self.driver.find_element(By.XPATH,"//p[text()='Invalid credentials']").text
        assert act_validation==exp_validation ,f"Expected '{exp_validation}' but got '{act_validation}'"





