from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

locators = {
    "NEXT_BUTTON": (By.ID, "idp-discovery-submit"),
    "PASSWORD_INPUT": (By.ID, "okta-signin-password"),
    "SIGN_IN": (By.ID, "okta-signin-submit"),
    "USER_NAME_INPUT": (By.ID, "idp-discovery-username"),
}

class SignInPage(BasePage):
    def __init__(self, driver):
        super(SignInPage, self).__init__(driver)
        self.page_url = "https://account.planet.com/"

    def fill_out_user_name(self, user_name: str) -> None:
        """
        it's used for typing into "user name/email address" field
        :param user_name: "example@gmail.com"
        :return: none
        """
        self.wait.until(EC.presence_of_element_located((By.ID, locators["USER_NAME_INPUT"][1]))).send_keys(user_name)

    def fill_out_user_password(self, password: str) -> None:
        """
        it's used for typing into password field
        :param password:
        :return: none
        """
        self.wait.until(EC.presence_of_element_located((By.ID, locators["PASSWORD_INPUT"][1]))).send_keys(password)

    def submit_sign_in(self) -> None:
        """
        it's used for submitting the given user name and password"
        :return: none
        """
        self.wait.until(EC.presence_of_element_located((By.ID, locators["SIGN_IN"][1]))).click()

    def submit_username(self) -> None:
        """
        it's used for submitting the given user name
        :return: none
        """
        self.wait.until(EC.presence_of_element_located((By.ID, locators["NEXT_BUTTON"][1]))).click()