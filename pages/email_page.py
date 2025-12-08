from playwright.sync_api import Page


class EmailPage:

    def __init__(self, page: Page):
        self.page = page
        self.to_email = page.get_by_test_id('to-email')
        self.subject = page.get_by_test_id('subject')
        self.body = page.get_by_test_id('body')
        self.attachment = page.get_by_test_id('attachment')
        self.send_email_button = page.get_by_test_id('send-email')
        self.email_status = page.get_by_test_id('email-status')
        self.logout_button = page.get_by_test_id('logout')

    def compose_email(self, to: str, subject: str, body: str):
        self.page.get_by_test_id(to).click()
        self.subject.fill(subject)
        self.body.fill(body)

    def attach_file(self, file_path: str):
        self.attachment.set_input_files(file_path)

    def send_email(self):
        self.send_email_button.click()

    def logout(self):
        self.logout_button.click()
