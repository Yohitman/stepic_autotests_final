from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def check_name_of_product(self):
        product_name_to_buy = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_to_check = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TO_CHECK).text
        assert product_name_to_buy == product_name_to_check, "{} != {}, product name isnt comparing".format(product_name_to_buy, product_name_to_check)

    def check_value_of_basket_equal_to_price(self):
        value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert value == price, "{} != {}, product price isnt equal to basket".format(value, price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but shouldnt be"

    def should_not_disappear_message(self):
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message disappeared, but it shouldnt"
