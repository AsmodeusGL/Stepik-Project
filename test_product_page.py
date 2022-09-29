import pytest

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

import time


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(f'{time.time()}@fakemail.org', '1664372877')
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = LoginPage(browser, link)
        page.open()
        page.add_product_from_product_page()
        page.register_new_user(f'{time.time()}@fakemail.org', '1664372877')
        page.should_be_authorized_user()


@pytest.mark.need_review
def test_quest_can_add_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.test_quest_can_add_product_to_basket_from_product_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_should_see_login_link_on_product_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_go_to_login_page_from_product_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.test_guest_cant_see_product_in_basket_opened_from_product_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.test_message_disappeared_after_adding_product_to_basket()
