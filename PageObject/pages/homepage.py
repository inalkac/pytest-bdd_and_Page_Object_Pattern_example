from PageObject.pages.base_page import BasePage
from PageObject.locators.locators import Locators

class HomePage(BasePage):
    def __init__(self, driver):
       super().__init__(driver)
        
    def clickLogo(self):
        BasePage.click(self, Locators.LOGO)
        return self.driver.current_url()

    def get_page_title(self):
        return self.driver.title

    def start_signin_flow(self):
        self.click(Locators.SIGNIN_BUTTON)

