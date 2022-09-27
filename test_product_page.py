import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', [number for number in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    if link == 7:
        pytest.xfail('')
    link = f'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
    page = ProductPage(browser, link)
    page.open()
    page.entry_test()
