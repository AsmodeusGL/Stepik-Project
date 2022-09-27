from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class AddToBasket:
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    ALERT_BASKET = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in')
    BASKET_FORM = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in')
