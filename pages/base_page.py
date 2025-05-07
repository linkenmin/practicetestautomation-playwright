from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_element_visible(self, locator, timeout: int = 5000):
        locator.wait_for(state="visible", timeout=timeout)

    def navigate_to(self, url: str):
        self.page.goto(url)
