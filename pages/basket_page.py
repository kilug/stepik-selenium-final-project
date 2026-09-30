from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty(self):
        message = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        )

        assert "Your basket is empty" in message.text, \
            "Basket is not empty"