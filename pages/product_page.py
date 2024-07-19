from .base_page import BasePage
from .locators import BasketNotifications, ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_title()
        self.should_be_product_price()
        self.should_be_product_gallery_of_images_carousel()
        self.should_be_instock_data()
        self.should_be_add_to_cart_button()
        self.should_be_product_description()
        self.should_be_product_info()
        self.should_be_product_reviews()
        self.should_be_add_review_button()


    def should_be_product_title(self):
        # Проверка наличия названия продукта
        assert self.is_element_present(*ProductPageLocators.TITLE), \
            "Title is not present on the Product page"

    def should_be_product_price(self):
        # Проверка наличия цены в основной части страницы под названием
        assert self.is_element_present(*ProductPageLocators.PRICE), \
            "Price is not present on the Product page"

    def should_be_product_gallery_of_images_carousel(self):
        # Проверка наличия карусели изображений продукта
        assert self.is_element_present(*ProductPageLocators.GALLEGY_OF_IMAGES_CAROUSEL), \
            "Gallery of images carousel is not present on the Product page"

        
    def should_be_instock_data(self):
        # Проверка наличия информации о наличии продукта на складе
        assert self.is_element_present(*ProductPageLocators.INSTOCK_AVAILABILITY), \
            "Instock availability information is not present on the Product page"

        
    def should_be_add_to_cart_button(self):
        # Проверка наличия кнопки "добавить в корзину"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), \
            "Add to cart button is not present on the Product page"

        
    def should_be_product_description(self):
        # Проверка наличия описания продукта
        assert self.is_element_present(*ProductPageLocators.DESCRIPTION_TITLE), \
            "Description Title is not present on the Product page"

        assert self.is_element_present(*ProductPageLocators.DESCRIPTION_TEXT), \
            "Description Text is not present on the Product page"

        
    def should_be_product_info(self):
        # Проверка наличия детального описания продукта
        assert self.is_element_present(*ProductPageLocators.INFORMATION), \
            "Product information is not present on the Product page"

        
    def should_be_product_reviews(self):
        # Проверка наличия блока с отзывами о продукте
        assert self.is_element_present(*ProductPageLocators.REVIEWS), \
            "Block with reviews is not present on the Product page"

        
    def should_be_add_review_button(self):
        # Проверка наличия кнопки "Добавить отзыв"
        assert self.is_element_present(*ProductPageLocators.WRITE_REVIEW_BUTTON), \
            "Write review button is not present on the Product page"
    

    def add_to_basket_click(self):
        # Добавление товара в корзину кликом по кнопке "Добавить в корзину"
        self.click_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
    

    def get_product_name(self):
        # Передает название продукта с его страницы
        return self.get_element_text(*ProductPageLocators.TITLE)
    

    def get_product_name_from_basket_notification(self):
        # Получает название продукта добавленного в корзину из уведомления о добавлении 
        # на странице продукта
        return self.get_element_text(*BasketNotifications.PRODUCT_TITLE_ADDED_TO_BASKET)

    @staticmethod
    def price_convertion_str_to_float(price_raw):
        # Преобразует строку с ценой и валютой в десятичную дробь
        price = ''
        for element in price_raw:
            if element.isdigit() or element == '.' or element == ',':
                if element == ',':
                    price += '.'
                else:
                    price += element
        return float(price)


    def get_product_price(self):
        # Передает цену продукта со его страницы
        return self.price_convertion_str_to_float(self.get_element_text(*ProductPageLocators.PRICE))

    
    def get_product_price_from_basket_notification(self):
        # Передает стоимость товаров в корзине из уведомления о добавлении в корзину
        # со страницы товара
        return self.price_convertion_str_to_float(self.get_element_text(*BasketNotifications.BASKET_TOTAL_PRICE))
         
