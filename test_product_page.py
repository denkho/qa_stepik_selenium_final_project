import pytest
from .pages.product_page import ProductPage
from .pages.ulrs import Urls


# def test_guest_can_go_to_product_page(browser):
#     page = ProductPage(browser, Urls.PRODUCT_URL)
#     page.open()
#     page.should_be_product_page()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_THE_SHELLCODERS_HANDBOOK_URL + Urls.PROMO_NEW_YEAR_URL)
    page.open()

    product_name_added_to_basket = page.get_product_name()
    product_price_added_to_basket = page.get_product_price()

    page.add_to_basket_click()
    page.solve_quiz_and_get_code()

    product_in_basket = page.get_product_name_from_basket_notification()
    price_of_product_in_basket = page.get_product_price_from_basket_notification()

    assert product_name_added_to_basket == product_in_basket, \
        f"The product added to basket was '{product_name_added_to_basket}', but it is '{product_in_basket}'"
    assert product_price_added_to_basket == price_of_product_in_basket, \
        f"The price of product added to basket was '{product_price_added_to_basket}', but it is '{price_of_product_in_basket}'"
    

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])
def test_guest_can_add_product_to_basket_02(browser, link):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()

    product_name_added_to_basket = page.get_product_name()
    product_price_added_to_basket = page.get_product_price()

    page.add_to_basket_click()

    page.solve_quiz_and_get_code()

    product_in_basket = page.get_product_name_from_basket_notification()
    price_of_product_in_basket = page.get_product_price_from_basket_notification()

    assert product_name_added_to_basket == product_in_basket, \
        f"The product added to basket was '{product_name_added_to_basket}', but it is '{product_in_basket}'"
    assert product_price_added_to_basket == price_of_product_in_basket, \
        f"The price of product added to basket was '{product_price_added_to_basket}', but it is '{price_of_product_in_basket}'"
