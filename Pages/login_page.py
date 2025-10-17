from selenium.webdriver.common.by import By


class Loginpage :


    username_text = (By.XPATH,"//input[@name='username']")
    password_text=(By.XPATH,"//input[@name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self,driver):
        self.driver =driver

    def enter_username(self,username):
        self.driver.find_element(*self.username_text).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_text).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def loginpage(self,username,password):
        self.driver.find_element(*self.username_text).send_keys(username)
        self.driver.find_element(*self.password_text).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        
