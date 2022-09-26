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
