from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        header_expected = "Basket"
        assert header_expected == self.get_element_text(*BasketPageLocators.BASKET_HEADER_TEXT)
        self.should_be_text_about_empty_basket()


    def should_be_text_about_empty_basket(self):
        text_expected = "Your basket is empty."
        assert text_expected in self.get_element_text(*BasketPageLocators.BASKET_IS_EMPTY_TEXT)