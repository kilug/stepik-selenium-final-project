from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET
        )
        button.click()

    def should_be_success_message(self, product_name):
        message = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                ProductPageLocators.SUCCESS_MESSAGE
            )
        )

        assert product_name in message.text, \
            "Product name is not presented in success message"

    def should_be_basket_total(self, product_price):
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        )

        assert product_price in basket_total.text, \
            "Product price is not presented in basket total"

    def get_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        )
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        return product_price.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message did not disappear"