from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage
# from utils.baseclass import Baseclass


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    SIGNIN_BUTTON = (By.XPATH, "//span[contains(text(), 'Account & Lists')]")
    SEARCH_BOX = (By.CSS_SELECTOR, "#twotabsearchtextbox")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#nav-search-submit-button")

    def Click_Sign_In(self):
        return self.find_element(*self.SIGNIN_BUTTON).click()

    def search_for_product(self, product_name):
        self.find_element(*self.SEARCH_BOX).send_keys(product_name)
        self.find_element(*self.SEARCH_BUTTON).click()


