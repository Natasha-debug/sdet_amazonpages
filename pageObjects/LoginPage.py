from selenium.webdriver.common.by import By
from utils.baseclass import Baseclass
from pageObjects.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    log_obj = Baseclass()

    EMAIL_INPUT = (By.XPATH, "//input[@id='ap_email']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id= 'ap_password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "input[id='signInSubmit']")

    def enter_email(self, email_id):
        self.find_element(*self.EMAIL_INPUT).send_keys(email_id)
        self.find_element(*self.CONTINUE_BUTTON).click()
        self.log_obj.get_Logger().info("click continue after entering email")

    def enter_password(self, user_pass):
        self.find_element(*self.PASSWORD_INPUT).send_keys(user_pass)
        self.find_element(*self.SIGN_IN_BUTTON).click()
        self.log_obj.get_Logger().info("click on sigh in button")
