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


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.col-sm-6.product_main')


class BasePageLocators:
    USER_ICON = (By.CLASS_NAME, "icon-user")
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")


class BasketPageLocators:
    BASKET_EMPTY = (By.CLASS_NAME, 'content_inner')
