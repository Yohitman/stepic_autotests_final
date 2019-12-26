from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        input_new_login = self.browser.find_element(*LoginPageLocators.NEW_LOGIN_FIELD)
        input_new_password = self.browser.find_element(*LoginPageLocators.NEW_PASSWORD_FIELD)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_NEW_PASSWORD)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)
        input_new_login.send_keys(email)
        input_new_password.send_keys(password)
        input_confirm_password.send_keys(password)
        submit_button.click()
