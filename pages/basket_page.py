from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def basket_has_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), "Basket is not empty!"

    def is_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "Message of empty basket is not present!"
