from .locators import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

    def is_login_in_url(self):
        try:
            return 'login' in self.browser.current_url
        except NoSuchElementException:
            return False

    def is_login_form(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

    def is_register_form(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def add_product_to_basket(self, how, what):
        try:
            self.browser.find_element(how, what).click()
            return True
        except NoSuchElementException:
            return False

    def should_be_login_link(self):
        try:
            return self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        except NoSuchElementException:
            return False

    def go_to_login_page(self):
        try:
            self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
            return True
        except NoSuchElementException:
            return False

    def go_to_basket_from_main_page(self):
        try:
            self.browser.find_element(*AddToBasket.BUTTON_GROUP).find_element(*AddToBasket.BUTTON_TAG).click()
        except NoSuchElementException:
            return False

    def should_be_basket_empty(self):
        try:
            return 'Your basket is empty.' in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        except NoSuchElementException:
            return False

    def go_to_basket_form_product_page(self):
        try:
            self.browser.find_element(*AddToBasket.BUTTON_GROUP).find_element(*AddToBasket.BUTTON_TAG).click()
        except NoSuchElementException:
            return False

    def register_form(self, email, password):
        try:
            self.go_to_login_page()
            register_form = self.browser.find_element(*RegisterPageLocators.REGISTER_FORM)
            register_form.find_element(*RegisterPageLocators.REGISTRATION_EMAIL).send_keys(email)
            register_form.find_element(*RegisterPageLocators.REGISTRATION_PASS1).send_keys(password)
            register_form.find_element(*RegisterPageLocators.REGISTRATION_PASS2).send_keys(password)
            self.browser.find_element(*RegisterPageLocators.REGISTRATION_SUBMIT).click()
            return True
        except NoSuchElementException:
            return False

    def should_be_authorized_user_from_register_form(self):
        return self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
