Feature: MoneyGaming Registration
  As a new player
  I want to be able to register with a secure password
  So that my account remains protected

  Scenario Outline: Password validation rules
    Given I am on the MoneyGaming registration page
    When I enter a password "<password>"
    And I confirm the password "<password>"
    And I submit the registration form
    Then I should see a message "<expected_message>"

    Examples:
      | password  | expected_message                                     |
      | abc       | Password must be at least 6 characters               |
      | abc123    | Password must contain at least one special character |
      | abc@      | Password must contain at least one number            |
      | abc123@   | Registration successful                              |
      | ab12@     | Password must be at least 6 characters               |
      | @123456   | Registration successful                              |
      |           | Password cannot be empty                             |
      | " "       | Password cannot be empty                             |
      | null      | Password cannot be null                              |
      | "    "    | Password cannot contain only spaces                  |
      | ""        | Password cannot be empty                             |             
