from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """""Object repository"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign in')]")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password?")

    """""Constructor of this page class"""
    def __init__(self, driver):
        super()._init_(driver)
        self.driver.get(TestData.BASE_URL)

    """""Page actions for login page"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_fgPass_link_exist(self):
        return self.is_visible(self.FORGOT_PASSWORD_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

