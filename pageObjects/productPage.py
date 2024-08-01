from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from utils.baseclass import Baseclass


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    log_obj = Baseclass()
    log = log_obj.get_Logger()

    ADD_TO_CART = (By.CSS_SELECTOR, "input[id='add-to-cart-button']")
    CART_COUNT = (By.XPATH, "//span[@id='nav-cart-count']")

    def add_to_cart(self):
        self.find_element(*self.ADD_TO_CART).click()

    def get_cart_count(self):
        return self.find_element(*self.CART_COUNT).text

