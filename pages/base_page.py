import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException


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

    def solve_quiz_and_get_code(self, how, what):
        try:
            self.browser.find_element(how, what).click()
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            self.browser.switch_to.alert.accept()
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented!")
        except NoSuchElementException:
            print("No element found!")

    def product_should_be_added_to_basket(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

    def product_name_should_be_in_message(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

    def name_should_be_in_message(self):
        try:
            return self.browser.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main')\
                .find_element(By.TAG_NAME, 'h1')\
                .text in self.browser.find_element(By.CSS_SELECTOR,
                                                   '.alert.alert-safe.alert-noicon.alert-success.fade.in').text
        except NoSuchElementException:
            return False

    def should_be_presented_basket_from(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

    def product_price_equals_basket_price(self):
        try:
            return self.browser.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main')\
                .find_element(By.TAG_NAME, 'p')\
                .text == self.browser.find_element(By.CSS_SELECTOR,
                                                   '.alert.alert-safe.alert-noicon.alert-info.fade.in')\
                .find_element(By.TAG_NAME, 'strong').text
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
