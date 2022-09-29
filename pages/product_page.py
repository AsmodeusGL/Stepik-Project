from .base_page import BasePage
from .locators import *


class ProductPage(BasePage):
    def test_guest_should_see_login_link_on_product_page(self):
        assert self.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self):
        assert self.go_to_login_page()

    def test_quest_can_add_product_to_basket_from_product_page(self):
        assert self.add_product_to_basket(*AddToBasket.ADD_BUTTON)

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.add_product_to_basket(*AddToBasket.ADD_BUTTON)
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message is not disappeared, but should be"
