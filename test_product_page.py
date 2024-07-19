import time
from .pages.product_page import ProductPage
from .pages.ulrs import Urls


# def test_guest_can_go_to_product_page(browser):
#     page = ProductPage(browser, Urls.PRODUCT_URL)
#     page.open()
#     page.should_be_product_page()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_URL + Urls.PROMO_URL)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_basket_click()
    page.solve_quiz_and_get_code()
