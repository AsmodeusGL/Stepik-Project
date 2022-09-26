from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

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
