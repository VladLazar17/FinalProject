Feature: Test the functionality of the Login Page

  Background:
    Given I am on the Login Page


  @simple
  #Scenariu1 fara parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email
    When I insert an unregistered email in the email input
    When I insert a password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error text contains "No customer account found" message

  @parameterzied
  #Scenariu1 cu paramentru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email
    When I insert "wrong_email@host.com" in the email input
    When I insert "parolaoarecare" in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error text contains "No customer account found"



