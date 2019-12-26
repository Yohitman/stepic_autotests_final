from pages.product_page import ProductPage
from pages.base_page import LoginPage
import time
import pytest

link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

#@pytest.mark.parametrize('offer_link', range(0,10))
def test_guest_can_add_product_to_basket(browser):#, offer_link):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(offer_link)
    page = ProductPage(browser, link1)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_of_product()
    page.check_value_of_basket_equal_to_price()
#    time.sleep(100)

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

@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        #создаем па API
        self.link = self.product.link
        yield
        self.product.delete()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.link2)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link2)
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

    #@pytest.mark.parametrize('offer_link', range(0,10))
    def test_user_can_add_product_to_basket(self, browser):#, offer_link):
    #    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(offer_link)
        page = ProductPage(browser, link1)
        page.open()
        page.click_add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_name_of_product()
        page.check_value_of_basket_equal_to_price()
    #    time.sleep(100)
