from PageObject.pages.base_page import BasePage
from PageObject.locators.locators import Locators

class LoginPage(BasePage):
    def __init__(self, driver):
       super().__init__(driver)
        
    def signin(self, username, password):
        self.fillout_field(Locators.USERNAME_TF, username)
        self.fillout_field(Locators.PWD_TF, password)
        self.click(Locators.LOGIN_BUTTON)

