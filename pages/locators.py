from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    TITLE = (By.CSS_SELECTOR, ".product_main>h1")
    PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    INSTOCK_AVAILABILITY = (By.CSS_SELECTOR, ".instock.availability")
    WRITE_REVIEW_BUTTON = (By.ID, "write_review")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    GALLEGY_OF_IMAGES_CAROUSEL = (By.ID, "product_gallery")
    DESCRIPTION_TITLE = (By.ID, "product_description")
    DESCRIPTION_TEXT = (By.CSS_SELECTOR, "#product_description+p")
    INFORMATION = (By.CSS_SELECTOR, ".table.table-striped")
    REVIEWS = (By.XPATH, "//section/div[@id='reviews']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasketNotifications():
    PRODUCT_TITLE_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
