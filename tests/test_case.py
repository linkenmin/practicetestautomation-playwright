import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

@pytest.mark.functional
def test_positive_login(browser_context):
    login_page = LoginPage(browser_context)
    login_page.open()
    login_page.is_ready()

    login_page.login("student", "Password123")

    secure_page = SecurePage(browser_context)
    secure_page.is_ready()
    secure_page.logout()

    login_page.is_ready()

@pytest.mark.negative
def test_negative_username(browser_context):
    login_page = LoginPage(browser_context)
    login_page.open()
    login_page.is_ready()

    login_page.login("incorrectUser", "Password123")
    actual = login_page.get_error_message_text()
    assert actual == "Your username is invalid!"

@pytest.mark.negative
def test_negative_password(browser_context):
    login_page = LoginPage(browser_context)
    login_page.open()
    login_page.is_ready()

    login_page.login("student", "incorrectPassword")
    actual = login_page.get_error_message_text()
    assert actual == "Your password is invalid!"