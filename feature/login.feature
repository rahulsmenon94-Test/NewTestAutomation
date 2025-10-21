Feature: login functionality

  Background: common steps
    Given the user is on the login page

  Scenario: Successful login with valid credentials 
    When the user enters valid credentials
    Then the user should be redirected to the dashboard
    
  Scenario Outline: Login with invalid credentials
    When user gives invalid username "<username>" and password "<password>"
    Then shows validation
    Examples:
    |username|password|
    |admin123|123|
    |abcd|admin|

