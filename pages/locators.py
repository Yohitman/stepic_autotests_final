from selenium.webdriver.common.by import By

class product_page_locators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_VALUE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_TO_CHECK = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class base_page_locators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span a")

class basket_page_locators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "#basket_formset")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
