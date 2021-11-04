from selenium.webdriver.common.by import By
class Locators():
   #Homepage
   LOGO = (By.XPATH, "//a[contains(@href, 'https://github.com/')]") 
   SIGNIN_BUTTON = (By.XPATH, "//header//a[contains(., 'Sign in')]")

   #Login page
   LOGIN_BUTTON = (By.NAME, "commit")
   USERNAME_TF = (By.ID, "login_field")
   PWD_TF = (By.ID, "password")