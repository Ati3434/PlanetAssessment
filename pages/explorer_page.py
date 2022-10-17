
from fixtures.params import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

locators = {
    "ITEMS_SAVED_SEARCHES_LIST": (By.CSS_SELECTOR, "[data-qe='search-list-item-title']"),
    "RESULTS_IN_SEARCH": (By.XPATH, "//*[@data-qe = 'search-input'][contains(@aria-activedescendant, 'option')]"),
    "SAVE_SEARCH_BUTTON_ON_DIALOG": (By.CSS_SELECTOR, "[data-cy = 'dialog-save-search-button']"),
    "SAVE_SEARCH_FIELD_ON_DIALOG": (By.CSS_SELECTOR, "[data-qe = 'save-search-name'] input"),
    "SAVE_SEARCH_TAB_ON_DAILY_S": (By.XPATH, "//*[@data-qe = 'click-save-search-button'][contains(text(), 'Save search')]"),
    "SEARCH_BUTTON": (By.CSS_SELECTOR, "[data-qe = 'search-input']"),
    "SKIP_BUTTON_ON_TRIAL": (By.CSS_SELECTOR, "[data-qe = 'skip-tour-button']"),
    "UPDATE_SEARCH_BUTTON_ON_DIALOG": (By.XPATH, "//*[@role = 'dialog']//button[contains(text(), 'Update')]"),
    "UPDATE_SEARCH_TAB_ON_DAILY_S": (By.XPATH, "//*[@data-qe = 'click-save-search-button'][contains(text(), 'Update search')]"),
}

class ExplorerPage(BasePage):
    def __init__(self, driver):
        super(ExplorerPage, self).__init__(driver)
        self.page_url = BASE_URL + "explorer/"

    def get_name_of_search_on_dialog(self) -> str:
        return self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locators["SAVE_SEARCH_FIELD_ON_DIALOG"][1]))).get_attribute(
            "value")

    def navigate_saving_current_search(self) -> None:
        """
        it's used for clicking the 'save search' tab on daily scenes
        :return:
        """
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators["SAVE_SEARCH_TAB_ON_DAILY_S"][1]))).click()

    def navigate_updating_saved_search(self) -> None:
        """
        it's used for clicking the 'update search' tab on daily scenes
        :return:
        """
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators["UPDATE_SEARCH_TAB_ON_DAILY_S"][1]))).click()


    def search_for_a_location(self, location: str) -> None:
        """
        it's used for searching and selecting the first/top given option from the results
        :return: none
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators["SEARCH_BUTTON"][1]))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locators["SEARCH_BUTTON"][1]))).send_keys(location)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators["RESULTS_IN_SEARCH"][1])))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locators["SEARCH_BUTTON"][1]))).send_keys(Keys.ENTER)

    def skip_the_trail(self) -> None:
        """
        it's used for skipping the trail option on 'welcome to planet explorer'
        :return:
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators["SKIP_BUTTON_ON_TRIAL"][1]))).click()

    def submit_save_search_on_dialog(self) -> None:
        """
        Submit the save search on the dialog
        :return:
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators["SAVE_SEARCH_BUTTON_ON_DIALOG"][1]))).click()

    def submit_update_search_on_dialog(self) -> None:
        """
        it's used for clicking the 'update search' tab on daily scenes
        :return:
        """
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators["UPDATE_SEARCH_BUTTON_ON_DIALOG"][1]))).click()
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, locators["UPDATE_SEARCH_BUTTON_ON_DIALOG"][1])))

    def update_the_name_on_dialog(self, name : str) -> None:
        """
        it's used for updating the name of saved search
        :param name:
        :return:
        """
        element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators["SAVE_SEARCH_FIELD_ON_DIALOG"][1])))
        element.send_keys(Keys.SHIFT, Keys.ARROW_UP)
        element.send_keys(Keys.DELETE)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators["SAVE_SEARCH_FIELD_ON_DIALOG"][1]))).send_keys(name)







