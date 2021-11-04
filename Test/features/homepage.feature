Feature: Homepage

    As a user
    i want to be able to navigate to Homepage
    So that I can access to all key features

Scenario: Open homepage
    Given I navigate to "HomePage"
    And "BASE_URL" is opened
    Then "HOMEPAGE_TITLE" can be observed