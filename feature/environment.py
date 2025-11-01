import json
import os
import time
from selenium import webdriver
from Pages.login_page import Loginpage
from Pages.users_page import Users_page
from utilities.read_properties import Read_config
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    # context.driver = webdriver.Firefox()
    # context.driver.maximize_window()
    options = Options()
    options.add_argument("--start-maximized")
        # Uncomment to run without opening browser:
        # options.add_argument("--headless")

        # Use Selenium Manager (no need for manual path)
    
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)

    context.login_url = Read_config.get_admin_page_url()
    context.username = Read_config.get_username()
    
    context.password = Read_config.get_password()
    context.login = Loginpage(context.driver)
    context.userpage=Users_page(context.driver)
    context.driver.implicitly_wait(10)



def before_all(context):
    with open("Test_data/users.json", "r") as f:
        test_data = json.load(f)
        context.test_list = test_data["users"] 

def after_step(context,step):
    if step.status == "failed": 
        os.makedirs("screenshots", exist_ok=True)
        timestamp =int(time.time())
        screenshot_name = f"screenshots/failed_{timestamp}.png"
        context.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved to {screenshot_name}")
        

def after_scenario(context, scenario):
    context.driver.quit()