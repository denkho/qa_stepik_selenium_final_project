from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # Проверка корректности ссылки
        url_expected = "login"
        url_fact = self.browser.current_url
        assert url_expected in url_fact, f"Current url is '{url_fact}', but it should be '{url_expected}'"


    def should_be_login_form(self):
        # Проверка наличия формы авторизации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"


    def should_be_register_form(self):
        # Проверка наличия формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"


    def register_new_user(self, email, password):
        """Регистрация нового пользователя

        Args:
            email (str): fake email for test
            password (str): fake password for test
        """        
        self.click_element(*BasePageLocators.LOGIN_LINK)
        self.add_text_to_input_field(*LoginPageLocators.REGISTRATION_EMAIL, email)
        self.add_text_to_input_field(*LoginPageLocators.REGISTRATION_PASSWORD_1, password)
        self.add_text_to_input_field(*LoginPageLocators.REGISTRATION_PASSWORD_2, password)
        self.click_element(*LoginPageLocators.REGISTRATION_BUTTON)

