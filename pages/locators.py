from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTRATION_EMAIL = (
        By.CSS_SELECTOR,
        "#id_registration-email"
    )

    REGISTRATION_PASSWORD = (
        By.CSS_SELECTOR,
        "#id_registration-password1"
    )

    REGISTRATION_PASSWORD_CONFIRM = (
        By.CSS_SELECTOR,
        "#id_registration-password2"
    )

    REGISTRATION_BUTTON = (
        By.CSS_SELECTOR,
        "[name='registration_submit']"
    )


class ProductPageLocators:
    ADD_TO_BASKET = (
        By.CSS_SELECTOR,
        ".btn-add-to-basket"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".alert-success"
    )

    BASKET_TOTAL = (
        By.CSS_SELECTOR,
        ".basket-mini"
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        ".product_main h1"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".product_main .price_color"
    )


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (
        By.XPATH,
        "//p[contains(text(), 'Your basket is empty')]"
    )