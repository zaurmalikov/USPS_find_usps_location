from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class FindUspsLocation:
    def __init__(self, driver):
        self.driver = driver

    find_location_text_box = (By.XPATH, "//input[@class='form-control location-search-input']")
    within_drop_down_menu = (By.XPATH, "//button[@id='within-select']")
    radius_one_mile = (By.XPATH, "//li/a[@data-value='1']")
    search_button = (By.XPATH, "//div/a[@id='searchLocations']")
    address_retrieved = (By.XPATH, "//p[@class='address']")

    def enter_zip_code(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.find_location_text_box))
        entry = self.driver.find_element(*FindUspsLocation.find_location_text_box)
        return entry

    def within_milage(self):
        self.driver.find_element(*FindUspsLocation.within_drop_down_menu).click()
        one_mile = self.driver.find_element(*FindUspsLocation.radius_one_mile)
        return one_mile.click()

    def search(self):
        search_btn = self.driver.find_element(*FindUspsLocation.search_button)
        return search_btn

    def retrieved_address(self):
        address = self.driver.find_element(*FindUspsLocation.address_retrieved).text
        return address
