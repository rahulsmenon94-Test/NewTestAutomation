import time
from behave import given, when, then
from selenium.webdriver.common.by import By


@given('the user is on the login page')
def enter_loginoage(context):
    context.driver.get(context.login_url)

@when('the user enters valid credentials')
def entered_credentials(context):
    context.login.loginpage(context.username, context.password)
  
@then('the user should be redirected to the dashboard')
def logged_inn(context):
    dashboard_text = context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    assert dashboard_text == "Dashboard", f"Expected 'Dashboard', but got '{dashboard_text}'"
    print(f"✅ Login successful: {dashboard_text}")
    
    
@when('user gives invalid username "{user}" and password "{pwd}"')
def invalid_credentials(context, user, pwd):
    print(f"🔐 Entering Username: {user}")
    print(f"🔐 Entering Password: {pwd}")
    context.login.loginpage(user, pwd)
@then('shows validation')
def validation_message(context):
    exp_validation = "Invalid credentials"
    act_validation = context.driver.find_element(By.XPATH, "//p[text()='Invalid credentials']").text
    assert act_validation == exp_validation, f" Expected '{exp_validation}' but got '{act_validation}'"
    print(f"✅ Validation message displayed: {act_validation}")
    
    