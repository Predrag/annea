Feature: Send email with attachment

  Scenario: User sends an email with an attachment to a contact and logs out
    Given the user is on the email login page
    When the user logs in with valid credentials email: "<email>" and password: "<password>"
    And the user creates a new email message to a contact "<to_email>"
    And the user attaches a file "<attachment_filename>" to the email
    And the user sends the email
    Then the email should be sent successfully with a status message
    And the user logs out

    Examples:
        | email          | password     | to_email             | attachment_filename | 
        | test@user.com  | password123  | test.user@gmail.com  | test_attachment.txt |
