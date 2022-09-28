from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_login_in_url(), 'Link has no attribute login!'

    def should_be_login_form(self):
        assert self.is_login_form(*LoginPageLocators.LOGIN_FORM), 'Current link has no login form!'

    def should_be_register_form(self):
        assert self.is_register_form(*LoginPageLocators.REGISTER_FORM), 'Current link has no register form!'

    def register_new_user(self, email, password):
        assert self.register_form(email, password)

    def should_be_authorized_user(self):
        assert self.should_be_authorized_user_from_register_form()

    def add_product_from_product_page(self):
        assert self.add_product_to_basket(*AddToBasket.ADD_BUTTON)
