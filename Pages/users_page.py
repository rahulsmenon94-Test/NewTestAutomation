
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Users_page :
    admin_select =(By.XPATH,"//span[text()='Admin']")
    add_button = (By.XPATH,"//button[text()=' Add ']")
    user_role_dropdown = (By.XPATH,"//div[@class='oxd-select-text oxd-select-text--active']")
    # select_ess =(By.XPATH,"//div[@class='oxd-select-text-input' and normalize-space()='ESS']")
    select_ess = (By.XPATH, "//div[contains(@class,'oxd-select-option') and normalize-space()='ESS']")
    employee_name_text = (By.XPATH,"//input[@placeholder='Type for hints...']")
    status_dropdown = (By.XPATH,"//label[normalize-space()='Status']/following::div[@class='oxd-select-text oxd-select-text--active'][1]")
    select_enabled=(By.XPATH, "//div[contains(@class,'oxd-select-option') and normalize-space()='Disabled']")
    username_name_text = (By.XPATH, "//label[normalize-space()='Username']/following::input[@class='oxd-input oxd-input--active'][1]")
    password_name_text=(By.XPATH,"//label[normalize-space()='Password']/following::input[@type='password'][1]")
    confirm_password_text=(By.XPATH,"//label[normalize-space()='Password']/following::input[@type='password'][2]")
    add_button_save=(By.XPATH, "//button[normalize-space()='Save']")
    def __init__(self,driver):
        self.driver =driver

    def click_admin(self):
        time.sleep(4)
        self.driver.find_element(*self.admin_select).click()
    def click_add_user(self,user):
        time.sleep(2)
        self.driver.find_element(*self.add_button).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.user_role_dropdown).click()
        
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.select_ess))
        
        self.driver.find_element(*self.select_ess).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.employee_name_text).send_keys(user["employee_name"])
        self.driver.implicitly_wait(10)
        employee_name = user["employee_name"]
        suggestion_locator = (By.XPATH, f"//div[@role='option' and contains(normalize-space(),'{employee_name}')]")
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(suggestion_locator)
        )
        self.driver.find_element(*suggestion_locator).click()
        self.driver.find_element(*self.status_dropdown).click()  
        self.driver.find_element(*self.select_enabled).click()
        self.driver.find_element(*self.username_name_text).send_keys(user["username"])
        self.driver.find_element(*self.password_name_text).send_keys(user["password"])
        self.driver.find_element(*self.confirm_password_text).send_keys(user["confirm_password"])
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.add_button_save).click()
        time.sleep(10)
        self.driver.find_element(*self.admin_select).click()
    
        
        # Additional methods for interacting with the Users page can be added here
          
    


