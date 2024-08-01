import time

import pytest

from pageObjects.HomePage import HomePage
from utils.baseclass import Baseclass
from pageObjects.LoginPage import LoginPage

from utils.configs import *
from pageObjects.SearchResultPage import SearchResultPage
from pageObjects.productPage import ProductPage


# @pytest.mark.usefixtures("setup")
class TestLogin(Baseclass):

    def test_login(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        search_results = SearchResultPage(self.driver)
        product_page = ProductPage(self.driver)
        log = self.get_Logger()

        home_page.Click_Sign_In()
        login_page.enter_email(USERNAME)
        login_page.enter_password(PASSWORD)
        log.info("Sign in successfully")

        home_page.search_for_product("wooden bed")
        search_results.click_first_product()
        time.sleep(5)

        product_page.add_to_cart()
        log.info("Product added to cart successfully")

        # assert int(product_page.get_cart_count())>0
        # log.info(f"cart count: {product_page.get_cart_count()}")




