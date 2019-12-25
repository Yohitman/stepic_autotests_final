from pages.main_page import main_page
import time
import pytest

link1 = "http://selenium1py.pythonanywhere.com/"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = main_page(browser, link1)
    page.open()
    page.go_to_basket_page()
    page.basket_has_no_products()
    page.is_message_basket_is_empty()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = main_page(browser, link2)
    page.open()
    page.go_to_basket_page()
    page.basket_has_no_products()
    page.is_message_basket_is_empty()
