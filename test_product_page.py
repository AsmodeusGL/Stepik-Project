import pytest
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    page.test_guest_cant_see_success_message()
    page.test_message_disappeared_after_adding_product_to_basket()
