import time

from .base_page import BasePage


class BasketPage(BasePage):
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self):
        self.go_to_basket_from_main_page()
        self.should_be_basket_empty()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        self.go_to_basket_form_product_page()
        self.should_be_basket_empty()
