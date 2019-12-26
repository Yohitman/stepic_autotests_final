from pages.main_page import MainPage
from pages.basket_page import BasketPage
import time
import pytest

link1 = "http://selenium1py.pythonanywhere.com/"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = BasketPage(browser, link1)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = BasketPage(browser, link1)
        page.open()
        page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link1)
    page.open()
    page.go_to_basket_page()
    page.basket_has_no_products()
    page.is_message_basket_is_empty()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link2)
    page.open()
    page.go_to_basket_page()
    page.basket_has_no_products()
    page.is_message_basket_is_empty()
