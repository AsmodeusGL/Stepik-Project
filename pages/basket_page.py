from pages.locators import *
from .base_page import BasePage


class BasketPage(BasePage):
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self):
        self.go_to_basket_from_main_page(*AddToBasket.BUTTON_GROUP, *AddToBasket.BUTTON_TAG)
        self.should_be_basket_empty(*BasketPageLocators.BASKET_EMPTY)

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        self.go_to_basket_form_product_page(*AddToBasket.BUTTON_GROUP, *AddToBasket.BUTTON_TAG)
        self.should_be_basket_empty(*BasketPageLocators.BASKET_EMPTY)
