from selenium.webdriver.common.by import By

class Users_page :
    admin_select =(By.XPATH,"//span[text()='Admin']")
    add_button = (By.XPATH,"//button[text()=' Add ']")
    user_role_dropdown = (By.XPATH,"div[class()='oxd-select-text oxd-select-text--active']")

    def __init__(self,driver):
        self.driver =driver

    def click_admin(self):
        self.driver.find_element(*self.admin_select).click()
    def click_add_user(self):
        self.driver.find_element(*self.add_button).click()
        self.driver.find_element(*self.user_role_dropdown).click()
        # Additional methods for interacting with the Users page can be added here
          
    


