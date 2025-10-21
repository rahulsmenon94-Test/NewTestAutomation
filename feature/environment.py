from selenium import webdriver
from Pages.login_page import Loginpage
from Pages.users_page import Users_page
from utilities.read_properties import Read_config

def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.login_url = Read_config.get_admin_page_url()
    context.username = Read_config.get_username()
    context.password = Read_config.get_password()
    context.login = Loginpage(context.driver)
    context.user=Users_page(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()