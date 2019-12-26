from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_VALUE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_TO_CHECK = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "#basket_formset")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    NEW_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    NEW_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_NEW_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".btn[value='Register']")
