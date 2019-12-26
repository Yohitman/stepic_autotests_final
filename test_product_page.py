from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
import time
import pytest


link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_of_product()
    page.check_value_of_basket_equal_to_price()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link2)
    page.open()
    page.go_to_basket_page()
    page.basket_has_no_products()
    page.is_message_basket_is_empty()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_disappear_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.go_to_login_page()

@pytest.mark.after_login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.link = login_link
        page = LoginPage(browser, self.link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.click_add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_name_of_product()
        page.check_value_of_basket_equal_to_price()
