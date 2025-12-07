
import os
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect

from pages.email_page import EmailPage
from pages.login_page import LoginPage

scenarios('features/send_email.feature')

to_email: str = 'test.user@gmail.com'
test_subject: str = 'Test Subject'
test_body: str = 'This is a test email body.'
attachment_filename: str = 'test_attachment.txt'


@given('the user is on the email login page')
def go_to_login(page: Page, base_url: str):
    page.goto(f'{base_url}/email_app.html')

@when(parsers.parse('the user logs in with valid credentials email: "{email}" and password: "{password}"'))
def login(login_page: LoginPage, email: str, password: str):
    login_page.login(email, password)

@when(parsers.parse('the user creates a new email message to a contact "{to_email}"'))
def create_email(email_page: EmailPage, to_email: str):
    email_page.compose_email(to_email, test_subject, test_body)
    expect(email_page.to_email).to_have_value(to_email)
    expect(email_page.subject).to_have_value(test_subject)
    expect(email_page.body).to_have_value(test_body)
    

@when(parsers.parse('the user attaches a file "{attachment_filename}" to the email'))
def attach_file(email_page: EmailPage, attachment_filename: str):
    file_path = os.path.abspath(f'tests/{attachment_filename}')
    email_page.attach_file(file_path)
    expect(email_page.attachment).not_to_be_empty()
    parsed_text = email_page.attachment.input_value().split('\\')[-1]
    assert parsed_text == attachment_filename

@when('the user sends the email')
def send_email(page: Page, email_page: EmailPage):
    email_page.send_email()
    

@then('the email should be sent successfully with a status message')
def email_sent(page: Page):
    email_status = page.get_by_test_id('email-status')
    expect(email_status).to_have_text(f'Email sent to {to_email} with attachment: {attachment_filename}')

@then('the user logs out')
def logout(page: Page, login_page: LoginPage):
    logout_button = page.get_by_test_id('logout')
    logout_button.click()
    expect(login_page.login_header).to_be_visible()

