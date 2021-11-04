Feature: Login
    As a user
    i want to be able to login
    So that I can browse my account homepage

    Scenario: Login with valid credentials
        Given I navigate to "LoginPage"
        And "LOGIN_PAGE_URL" is opened
        When Login using "USERNAME" and "PASSWORD"
        Then "ACCOUNT_HOMEPAGE_URL" opens

    Scenario: Login with invalid username
        Given I navigate to "LoginPage"
        And "LOGIN_PAGE_URL" is opened
        When Login using "INVALID_USERNAME" and "PASSWORD"
        Then "SIGNIN_FAIL_URL" opens

    Scenario: Login with invalid password
        Given I navigate to "LoginPage"
        And "LOGIN_PAGE_URL" is opened
        When Login using "USERNAME" and "INVALID_PASSWORD"
        Then "SIGNIN_FAIL_URL" opens

    