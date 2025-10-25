
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
    select_enabled=(By.XPATH, "//div[contains(@class,'oxd-select-option') and normalize-space()='Enabled']")
    select_disabled=(By.XPATH, "//div[contains(@class,'oxd-select-option') and normalize-space()='Disabled']")
    username_name_text = (By.XPATH, "//label[normalize-space()='Username']/following::input[@class='oxd-input oxd-input--active'][1]")
    password_name_text=(By.XPATH,"//label[normalize-space()='Password']/following::input[@type='password'][1]")
    confirm_password_text=(By.XPATH,"//label[normalize-space()='Password']/following::input[@type='password'][2]")
    add_button_save=(By.XPATH, "//button[normalize-space()='Save']")
    checkbox = (By.XPATH, "//i[contains(@class, 'oxd-checkbox-input-icon')]")
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
        
    

           
    def click_edit_button_by_username(self, username):
        print(f"🔍 Searching for username: '{username}'")

    # Locate the row that contains the username
        row_xpath = f"//div[contains(@class,'oxd-table-cell') and normalize-space()='{username}']/ancestor::div[contains(@class,'oxd-table-row')]"
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, row_xpath))
    )
        row_element = self.driver.find_element(By.XPATH, row_xpath)

    # Find the edit button inside that row only
        edit_button = row_element.find_element(By.XPATH, ".//button[contains(@class,'oxd-icon-button') and .//i[contains(@class,'bi-pencil-fill')]]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)
        time.sleep(1)
        edit_button.click()
        time.sleep(2)

    def edit_user(self):
        self.driver.find_element(*self.status_dropdown).click()
        self.driver.find_element(*self.select_disabled).click()
        self.driver.find_element(*self.add_button_save).click()
        time.sleep(4)


