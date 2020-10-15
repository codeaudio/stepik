from .pages.main_page import MainPage
from selenium.common.exceptions import NoAlertPresentException
import pytest
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page_from_product_page(self, browser):
    page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

def test_guest_should_see_login_link(self, browser):
    page = ProductPage(browser, self.link)
    # дальше обычная реализация теста