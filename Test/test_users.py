from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.read_properties import Read_config
from Demo.Pages.login_page import Loginpage

from Demo.Pages.users_page import Users_page


class Test02admin :
    loginurl=Read_config.get_admin_page_url()
    username =Read_config.get_username()
    password =Read_config.get_password()

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.userpage= Users_page(self.driver)
        self.login =Loginpage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_add_user(self):
        self.driver.get(self.loginurl)
        self.driver.implicitly_wait(10)
        self.login.loginpage(self.username,self.password)
        self.driver.implicitly_wait(10)
        self.userpage.click_admin()
        act_validation = self.driver.find_element(By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']//h6[text()='User Management']").text
        exp_validation ="User Management"
        assert act_validation==exp_validation,f"expected '{exp_validation}', but got '{act_validation}'"



