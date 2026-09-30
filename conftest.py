import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language"
    )


@pytest.fixture
def browser(request):
    language = request.config.getoption("language")

    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {"intl.accept_languages": language}
    )

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()


@pytest.fixture
def user(browser):
    email = str(time.time()) + "@fakemail.org"
    password = "Password123!"

    from pages.login_page import LoginPage

    login_page = LoginPage(
        browser,
        "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    )

    login_page.open()
    login_page.register_new_user(email, password)
    login_page.should_be_authorized_user()

    return email, password