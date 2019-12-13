from pages.product_page import product_page
import time
import pytest

@pytest.mark.parametrize('offer_link', range(0,10))
def test_guest_can_add_product_to_basket(browser, offer_link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(offer_link)
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = product_page(browser, link)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_of_product()
    page.check_value_of_basket_equal_to_price()
