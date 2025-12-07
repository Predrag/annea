
import os
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

scenarios('features/send_email_with_attachment.feature')

@given('the user is on the email login page')
def go_to_login(page: Page, base_url: str):
    page.goto(f'{base_url}/simple_email_app.html')  # Adjust URL as needed

@when('the user logs in with valid credentials')
def login(page: Page):
    email_input = page.get_by_test_id('email')
    email_input.fill('test@user.com')
    password = page.get_by_test_id('password')
    password.fill('password123')
    page.get_by_test_id('submit').click()

@when('the user creates a new email message to a contact')
def create_email(page: Page):
    # page.click('button.compose')
    email = page.get_by_test_id('to-email')
    email.fill('test.email@gmail.com')  # Contact from address book
    subject = page.get_by_test_id('subject')
    subject.fill('Test Subject')
    body = page.get_by_test_id('body')
    body.fill('Test email body.')

@when('the user attaches a file to the email')
def attach_file(page: Page):
    file_path = os.path.abspath('tests/test_attachment.txt')
    attachment = page.get_by_test_id('attachment')
    attachment.set_input_files(file_path)
    expect(attachment).to_have_value('test_attachment.txt')  # Verify attachment

@when('the user sends the email')
def send_email(page: Page):
    send_email = page.get_by_test_id('send-email')
    send_email.click()

@then('the email should be sent successfully')
def email_sent(page: Page):
    email_status = page.get_by_test_id('email-status')
    expect(email_status).to_have_text('Email sent to test@user.com with attachment: test_attachment.txt!')

@then('the user logs out')
def logout(page: Page):
    logout_button = page.get_by_test_id('logout')
    logout_button.click()

