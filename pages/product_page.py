from .base_page import base_page
from selenium.webdriver.common.by import By
from .locators import product_page_locators


class product_page(base_page):
    def click_add_to_basket(self):
        button = self.browser.find_element(*product_page_locators.ADD_BUTTON)
        button.click()

    def check_name_of_product(self):
        product_name_to_buy = self.browser.find_element(*product_page_locators.PRODUCT_NAME).text
        product_name_to_check = self.browser.find_element(*product_page_locators.PRODUCT_NAME_TO_CHECK).text
        assert product_name_to_buy == product_name_to_check, "{} != {}, product name isnt comparing".format(product_name_to_buy, product_name_to_check)

    def check_value_of_basket_equal_to_price(self):
        value = self.browser.find_element(*product_page_locators.BASKET_VALUE).text
        price = self.browser.find_element(*product_page_locators.PRICE).text
        assert value == price, "{} != {}, product price isnt equal to basket".format(value, price)
