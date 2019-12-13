from selenium.webdriver.common.by import By

class product_page_locators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_VALUE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_TO_CHECK = (By.CSS_SELECTOR, ".alert-success .alertinner strong")