from behave import given, when, then
from selenium.webdriver.common.by import By
from Pages.login_page import Loginpage

@given('the user is on the login page')
def enter_loginoage(context):
    context.driver.get(context.login_url)

@when('the user enters valid credentials')
def entered_credentials(context):
    context.login.loginpage(context.username, context.password)
  

@when('clicks the login button')
def step_impl(context):
    context.login.click_login()

@then('the user should be redirected to the dashboard')
def logged_inn(context):
    dashboard_text = context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    assert dashboard_text == "Dashboard", f"❌ Expected 'Dashboard', but got '{dashboard_text}'"
    print(f"✅ Login successful: {dashboard_text}")