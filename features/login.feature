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
  Scenario: Check that “Wrong email” message is displayed when the user enters an email address with an invalid format
    When I insert "emailinvalid" in the email input
    When I insert "parolainvalida" in the password input
    When I click on the login button
    Then The email error message is displayed
    Then The email error message text contains "Wrong email"

  @simple
  Scenario: Check that the URL is correct
    Then The actual URL is "https://demo.nopcommerce.com/login"

