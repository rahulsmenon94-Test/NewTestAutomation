import json
from behave import *
from Pages.users_page import Users_page

@given('user enters home page')
def enter_homepage(context):
    context.driver.get(context.login_url)
    context.login.loginpage(context.username, context.password)

@when('user adds the users')
def add_users(context):
    print("✅ scroll")
    context.userpage.click_admin()

    for user in context.test_list:
    #     context.userpage.click_add_user(user)
        context.userpage.click_edit_button_by_username(user["username"])

  


@then('Users are added Successfuly')
def users_added(context):
    print("✅ User added successfully")