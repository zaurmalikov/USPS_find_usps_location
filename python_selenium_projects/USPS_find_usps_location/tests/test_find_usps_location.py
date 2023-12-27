import pytest
from page_objects.home_page import HomePage
from selenium.common import NoSuchElementException
from test_data.zip_code_data import ZipCode
from utilities.base_class import BaseClass


class TestFindUspsLocation(BaseClass):
    @pytest.fixture(params=ZipCode.zip_code)
    def zip_code(self, request):
        return request.param

    def test_find_usps_location(self, zip_code):
        home_page = HomePage(self.driver)
        log = self.get_logger()

        log.info("Step 1 -- navigate to quick tools menu and click on FInd USPS Location icon")
        home_page.move_to_quick_tools_menu()
        find_usps_location_page = home_page.click_on_find_usps_location_icon()

        log.info("Step 2 -- Enter required ZIP Code, make radius 1 mile and click Find button")
        find_usps_location_page.enter_zip_code().send_keys(zip_code["PGH zip code"])
        find_usps_location_page.within_milage()
        find_usps_location_page.search().click()

        log.info("Step 3 -- Validating expected result")
        address = find_usps_location_page.retrieved_address()

        try:
            assert "13 WABASH ST PITTSBURGH, PA 15220-9998abc" in address, log.error("Expected address was not appear")
            log.info("Result validated as expected")
            self.driver.get_screenshot_as_file("screenshotPass.png")
        except AssertionError as e:
            self.driver.get_screenshot_as_file("screenshotFail.png")
            log.info(f"{e}")


