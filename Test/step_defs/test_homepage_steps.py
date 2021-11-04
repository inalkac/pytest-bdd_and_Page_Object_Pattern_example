#from Test.step_defs.conftest import test_data
from pytest_bdd import scenario, given, when, then, parsers
from PageObject.pages.homepage import HomePage



@scenario('../features/homepage.feature','Open homepage')
def test_open_homepage():
    pass

@then(parsers.parse('"{page_title}" can be observed'))
def page_title(browser_instance, page_title, data):
    assert browser_instance.get_title() in data[page_title]
