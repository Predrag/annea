from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_header = page.get_by_test_id('login-header')
        self.email_input = page.get_by_test_id('email')
        self.password_input = page.get_by_test_id('password')
        self.submit_button = page.get_by_test_id('submit')

    def login(self, email: str, password: str):
        expect(self.login_header).to_be_visible()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        expect(self.login_header).not_to_be_visible()