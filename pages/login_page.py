from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.submit = page.locator("#submit")
        self.error_message = page.locator("#error")

    def open(self):
        self.navigate_to(self.URL)

    def is_ready(self):
        self.wait_for_element_visible(self.username)
        self.wait_for_element_visible(self.password)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()

    def get_error_message_text(self) -> str:
        self.wait_for_element_visible(self.error_message)
        return self.error_message.inner_text()
