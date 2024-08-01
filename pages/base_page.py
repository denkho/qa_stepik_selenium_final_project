import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)


    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()


    def should_be_login_link(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    

    def click_element(self, how, what):
        """
        Функция для клика по элементу.
        how - как ищется селектор; 
        what - локатор
        """
        try:
            self.browser.find_element(how, what).click()
        except NoSuchElementException:
            print("Cannot click on the element which is not on the page")



    def add_text_to_input_field(self, how, what, data):
        """
        Функция для заполнения поля ввода.
        how - как ищется селектор; 
        what - локатор;
        data - что вводится в поле ввода
        """
        try:
            self.broser.find_element(how, what).send_keys(data)
        except NoSuchElementException:
            print("There is not such element to fill in the data into")


    def get_element_text(self, how, what):
        try:
            return self.browser.find_element(how, what).text
        except NoSuchElementException:
            print("There is not such element or text")



    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"

    def go_to_basket_page(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()
        except NoSuchElementException:
            print("There is no basket button or it has been changed")


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
