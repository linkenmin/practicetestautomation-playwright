import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

class TestLoginFlow:

    @pytest.fixture(autouse=True)
    def setup(self, browser_context):
        self.page = browser_context
        self.login_page = LoginPage(self.page)
        self.secure_page = SecurePage(self.page)

        self.login_page.open()
        self.login_page.is_ready()

    @pytest.mark.functional
    def test_positive_login(self):
        self.login_page.login("student", "Password123")
        self.secure_page.is_ready()
        self.secure_page.logout()
        self.login_page.is_ready()

    @pytest.mark.negative
    def test_negative_username(self):
        self.login_page.login("incorrectUser", "Password123")
        actual = self.login_page.get_error_message_text()
        assert actual == "Your username is invalid!"

    @pytest.mark.negative
    def test_negative_password(self):
        self.login_page.login("student", "incorrectPassword")
        actual = self.login_page.get_error_message_text()
        assert actual == "Your password is invalid!"
