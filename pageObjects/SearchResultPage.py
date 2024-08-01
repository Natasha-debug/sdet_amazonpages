from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class SearchResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    SEARCH_FIRST_PRODUCT = (By.XPATH, "//span[@data-component-type='s-search-results']/div/div[4]")

    def click_first_product(self):
        self.find_element(*self.SEARCH_FIRST_PRODUCT).click()
