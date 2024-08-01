import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.ulrs import Urls


def test_guest_can_go_to_product_page(browser):
    page = ProductPage(browser, Urls.PRODUCT_CODERS_AT_WORK)
    page.open()
    page.should_be_product_page()


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


@pytest.mark.xfail(reason="should fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_CODERS_AT_WORK)
    page.open()
    page.add_to_basket_click()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Urls.PRODUCT_CODERS_AT_WORK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="the success message doesn't disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_CODERS_AT_WORK)
    page.open()
    page.add_to_basket_click()
    assert not page.should_be_disapeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    pass
