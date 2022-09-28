from pages.product_page import ProductPage
from pages.basket_page import BasketPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_should_see_login_link_on_product_page()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_go_to_login_page_from_product_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.test_guest_cant_see_product_in_basket_opened_from_product_page()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.test_guest_cant_see_success_message_after_adding_product_to_basket()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.test_guest_cant_see_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.test_message_disappeared_after_adding_product_to_basket()
