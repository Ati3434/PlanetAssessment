from fixtures.params import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

locators = {
    "PLANET_EXPLORER_LINK": (By.XPATH, "//a[contains(text(), 'Planet Explorer')]"),
}

class AccountDashboardPage(BasePage):
    def __init__(self, driver):
        super(AccountDashboardPage, self).__init__(driver)
        self.page_url = BASE_URL + "account/#/dashboard"

    def select_planet_explorer(self) -> None:
        """
        it's used for selecting 'planet explorer' under the planet applications
        :return: none
        """
        original_window = self.driver.current_window_handle
        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators["PLANET_EXPLORER_LINK"][1]))).click()
        self.wait.until(EC.number_of_windows_to_be(2))
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break