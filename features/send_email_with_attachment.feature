Feature: Send email with attachment

  Scenario: User sends an email with an attachment to a contact and logs out
    Given the user is on the email login page
    When the user logs in with valid credentials
    And the user creates a new email message to a contact
    And the user attaches a file to the email
    And the user sends the email
    Then the email should be sent successfully
    And the user logs out
