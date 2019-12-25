from .base_page import base_page
from selenium.webdriver.common.by import By
from .locators import basket_page_locators

class main_page(base_page):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def basket_has_no_products(self):
        assert self.is_not_element_present(*basket_page_locators.BASKET_CONTENT), "Basket is not empty!"

    def is_message_basket_is_empty(self):
        assert self.is_element_present(*basket_page_locators.MESSAGE_EMPTY_BASKET), "Message of empty basket is not present!"
