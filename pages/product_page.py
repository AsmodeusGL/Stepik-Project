from .base_page import BasePage
from .locators import *


class ProductPage(BasePage):
    def entry_test(self):
        self.solve_quiz_and_get_code(*AddToBasket.ADD_BUTTON)
        self.message_product_should_be_added_to_basket()
        self.product_name_should_be_in_message_before_added_product_to_basket()
        self.should_be_presented_basket_message_with_price()
        self.product_price_should_be_basket_price()

    def message_product_should_be_added_to_basket(self):
        assert self.product_should_be_added_to_basket(*AddToBasket.ALERT_BASKET), \
            "Product has no been added to your basket."

    def product_name_should_be_in_message_before_added_product_to_basket(self):
        assert self.name_should_be_in_message(), \
            "Product name should be in added product name"

    def should_be_presented_basket_message_with_price(self):
        assert self.should_be_presented_basket_from(*AddToBasket.BASKET_FORM), \
            "Should be presented basket form"

    def product_price_should_be_basket_price(self):
        assert self.product_price_equals_basket_price(), \
            "Product price should be equals basket price"
