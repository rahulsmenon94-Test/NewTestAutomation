from behave import *
from selenium.webdriver.common.by import By
from Pages.users_page import Users_page

@given('user enters home page')
def enter_homepage(context):
    context.driver.get(context.login_url)
    context.login.loginpage(context.username, context.password)
@when('user adds the users')
def add_users(context):    
    context.user.click_admin()
    context.user.click_add_user()
    
@then('Users are added Successfuly')    
def users_added(context):
    print("✅ User added successfully")
    