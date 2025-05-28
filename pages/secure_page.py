from playwright.sync_api import Page
from pages.base_page import BasePage

class SecurePage(BasePage):
    URL = "https://practicetestautomation.com/logged-in-successfully/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.logout_button = page.locator("text=Log out")

    def is_ready(self):
        self.wait_for_element_visible(self.logout_button)

    def logout(self):
        self.logout_button.click()
