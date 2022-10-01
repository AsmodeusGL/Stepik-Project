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

    def should_be_login_link(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

    def go_to_login_page(self, how, what):
        try:
            self.browser.find_element(how, what).click()
            return True
        except NoSuchElementException:
            return False

    def go_to_basket_from_main_page(self, how_1, what_1, how_2, what_2):
        try:
            self.browser.find_element(how_1, what_1).find_element(how_2, what_2).click()
        except NoSuchElementException:
            return False

    def should_be_basket_empty(self, how, what):
        try:
            return 'Your basket is empty.' in self.browser.find_element(how, what).text
        except NoSuchElementException:
            return False

    def go_to_basket_form_product_page(self, how_1, what_1, how_2, what_2):
        try:
            self.browser.find_element(how_1, what_1).find_element(how_2, what_2).click()
        except NoSuchElementException:
            return False

    def register_form(self, email, password, content):
        try:
            register_form = self.browser.find_element(content[0], content[1])
            register_form.find_element(content[2], content[3]).send_keys(email)
            register_form.find_element(content[4], content[5]).send_keys(password)
            register_form.find_element(content[6], content[7]).send_keys(password)
            self.browser.find_element(content[8], content[9]).click()
            return True
        except NoSuchElementException:
            return False

    def should_be_authorized_user_from_register_form(self, how, what):
        return self.is_element_present(how, what), \
            "User icon is not presented, probably unauthorised user"
