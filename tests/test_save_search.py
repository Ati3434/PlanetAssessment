
import unittest
import random
from fixtures.base import Base
from pages.sign_in_page import SignInPage
from pages.explorer_page import ExplorerPage

class SaveSearchCases(Base):
    def setUp(self):
        super(SaveSearchCases, self).setUp()
        self.sign_in = SignInPage(self.driver)
        self.explorer = ExplorerPage(self.driver)
        self.user_name = "kose.atak@gmail.com"
        self.user_password = "PlanetAti3434?"

    # Verify that saving search and updating
    def test_save_search_and_update(self):
        location = "San francisco, CA"
        self.explorer.go_to_page()
        self.sign_in.fill_out_user_name(self.user_name)
        self.sign_in.submit_username()
        self.sign_in.fill_out_user_password(self.user_password)
        self.sign_in.submit_sign_in()
        # Test is written for a new user that have a trail option
        self.explorer.skip_the_trail()
        self.explorer.search_for_a_location(location)
        self.explorer.navigate_saving_current_search()
        default_name = self.explorer.get_name_of_search_on_dialog()
        assert default_name in location.title()
        self.explorer.submit_save_search_on_dialog()
        self.explorer.navigate_updating_saved_search()
        name = "name is updated " + str(random.randint(1000, 9999))
        self.explorer.update_the_name_on_dialog(name)
        self.explorer.submit_update_search_on_dialog()

        # Verify that saving search with renaming default name and updating
        # def test_save_search_with_naming_search_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click Save search and update the default name
            # Update Save search

        # Verify that saving search doesn't accept existing saved search name
        # def test_save_search_with_naming_existing_search_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click Save search and update the default name as exiting search name
            # Verify that error message and save search
            # Update Save search

        # Verify that saving search doesn't accept empty search name
        # def test_save_search_with_empty_search_name_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click Save search and update the default name as empty
            # Verify that error message and save search
            # Update Save search

        # Verify that saving search with disabling notification and updating
        # def test_save_search_with_disable_notification_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click Save search with disable notifications
            # Update Save search

        # Verify that saving search with adding a folder and updating
        # def test_save_search_with_adding_folder_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click Save search with adding folder/folders
            # Update Save search

        # Verify that saving search doesn't accept existing folder name
        # def test_save_search_with_adding_existing_folder_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click Save search with adding existing folder name
            # Verify that message and save search

        # Verify that saving search with selecting a date range and updating
        # def test_save_search_with_date_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click dates and select a date range on the calendar
            # Click Save search and verify selected date range on the dialog
            # Update Save search

        # Verify that saving search with 'no end date' and updating
        # def test_save_search_with_no_end_date_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click dates and select a range on the calendar
            # Click Save search and select 'no end date'
            # verify range of date doesn't have the end date
            # Update Save search

        # Verify that saving search with imagery type and updating
        # def test_save_search_with_imagery_type_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click filter and select a imagery type
            # Click Save search and verify selected imagery type in satellite constellations
            # Update Save search

        # Verify that saving search with planetscope filter and updating
        # def test_save_search_with_planetscope_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click filter and select a imagery type
            # Click Save search and verify selected planetscope filter in satellite constellations
            # Update Save search

        # Verify that saving search with environmental conditions and updating
        # def test_save_search_with_environmental_conditions_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click filter and change environmental conditions
            # Click Save search and verify changes in filters
            # Update Save search

        # Verify that saving search with advanced filter and updating
        # def test_save_search_with_advanced_filter_and_update(self):
            # Login to Planet explorer(www.planet.com/explorer)
            # Click search button, search for a city
            # Click filter and change advanced filters
            # Click Save search and verify changes in filters
            # Update Save search



if __name__ == '__main__':
    unittest.main()