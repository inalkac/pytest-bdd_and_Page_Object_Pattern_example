import os
import sys
from typing import ClassVar
import pytest
import json
from selenium import webdriver
from pytest_bdd import scenario, given, when, then, parsers
# page objects
from PageObject.pages.base_page import BasePage
from PageObject.pages.homepage import HomePage
from PageObject.pages.login_page import LoginPage



@pytest.fixture
def browser_config(scope ='session'):
    with open("config.json", 'r') as config_file:
        config = json.load(config_file)
    assert config["browser"]  in ["Chrome", "Firefox", "Headless Chrome"]
    return config

# fixture to create browser instance
@pytest.fixture
def browser(browser_config):
    if browser_config["browser"] == "Chrome":
        driver = webdriver.Chrome(executable_path = f"{os.curdir}/webdrivers/chromedriver.exe")
    elif browser_config["browser"] == "Firefox":
        driver = webdriver.Firefox(executable_path = f"{os.curdir}/webdrivers/geckodriver.exe")
    elif browser_config["browser"] == "Headless Chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument("headless")
        driver = webdriver.Chrome(executable_path = f"{os.curdir}/webdrivers/chromedriver.exe", options = opts)
    else:
        raise Exception(f"browser configuration {browser_config['browser']}, defined in config.json, is not supported")
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    driver.quit()

# fixture to pass test data to steps
@pytest.fixture
def data(scope = 'session'):
    with open("PageObject/test_data/data.json", 'r', encoding="UTF-8") as data_file:
        data = json.load(data_file)
    return data

# common used steps    

@given(parsers.parse('I navigate to "{PageObject}"'), target_fixture='browser_instance')
def browser_instance(browser, PageObject):
    class_name = getattr(sys.modules[__name__], PageObject)
    page = class_name(browser)
    return page

@given(parsers.parse('"{url}" is opened'))
def open_url(browser_instance, data, url):
    browser_instance.openURL(data[url])

@then(parsers.parse('"{page_url}" opens'))
def observe_page(browser_instance, data, page_url):
    assert browser_instance.get_page_url() in data[page_url]