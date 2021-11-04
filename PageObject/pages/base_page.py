"""
this file will contain BasePage class  with properties like find element, click ets.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_page_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def openURL(self, URL):
        self.driver.get(URL)

    def getElement(self, by_locator): 
        return self.wait.until(EC.presence_of_element_located(by_locator))
        
    def click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()
        
    def fillout_field(self, by_locator, text):
        txt_field = self.wait.until(EC.presence_of_element_located(by_locator))
        txt_field.send_keys(text)