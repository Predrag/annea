
import os
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page

scenarios('features/send_email_with_attachment.feature')

@given('the user is on the email login page')
def go_to_login(page: Page):
    page.goto('https://your-email-provider.com/login')

@when('the user logs in with valid credentials')
def login(page: Page):
    page.fill('input[name="email"]', 'your_email@example.com')
    page.fill('input[name="password"]', 'your_password')
    page.click('button[type="submit"]')

@when('the user creates a new email message to a contact')
def create_email(page: Page):
    page.click('button.compose')
    page.fill('input.to', 'your_email@example.com')  # Contact from address book
    page.fill('input.subject', 'Test Subject')
    page.fill('textarea.body', 'Test email body.')

@when('the user attaches a file to the email')
def attach_file(page: Page):
    file_path = os.path.abspath('tests/test_attachment.txt')
    page.set_input_files('input[type="file"]', file_path)

@when('the user sends the email')
def send_email(page: Page):
    page.click('button.send')

@then('the email should be sent successfully')
def email_sent(page: Page):
    assert page.is_visible('text=Email sent')  # Adjust selector as needed

@then('the user logs out')
def logout(page: Page):
    page.click('button.logout')
