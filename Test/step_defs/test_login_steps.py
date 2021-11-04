#from Test.step_defs.conftest import test_data
from pytest_bdd import scenario, given, when, then, parsers
from PageObject.pages.login_page import LoginPage


@scenario('../features/login.feature', 'Login with valid credentials')
def test_login_valid_credentials():
    pass
@scenario('../features/login.feature', 'Login with invalid username')
def test_login_invalid_username():
    pass
@scenario('../features/login.feature', 'Login with invalid password')
def test_login_invalid_password():
    pass


@when(parsers.parse('Login using "{username}" and "{password}"'))
def login(browser_instance, data, username, password):
    browser_instance.signin(data[username], data[password])

