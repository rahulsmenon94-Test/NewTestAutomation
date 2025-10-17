from selenium.webdriver.common.by import By

class Users_page :
    admin_select =(By.XPATH,"//span[text()='Admin']")

    def __init__(self,driver):
        self.driver =driver

    def click_admin(self):
        self.driver.find_element(*self.admin_select).click()




