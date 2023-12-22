from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_objects.find_usps_locations_page import FindUspsLocation


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    quick_tools_menu_icon = (By.XPATH, "//li/a[@class='nav-first-element menuitem']")
    quick_tools_menu_instance = (By.XPATH, "//li[@class='qt-nav menuheader']/div/ul[@role='menu']/li")
    find_usps_location_text = (By.XPATH, "//div/h1[text()='Find USPS Locations']")

    def move_to_quick_tools_menu(self):
        action_chain = ActionChains(self.driver)
        move = action_chain.move_to_element(self.driver.find_element(*HomePage.quick_tools_menu_icon)).perform()
        return move

    def click_on_find_usps_location_icon(self):
        menu_instances = self.driver.find_elements(*HomePage.quick_tools_menu_instance)
        for menu_instance in menu_instances:
            if "Find USPS Locations" in menu_instance.text:
                menu_instance.click()
                assertion_element = self.driver.find_element(*HomePage.find_usps_location_text).text
                assert "Find USPS Locations" in assertion_element
                break
        find_usps_location = FindUspsLocation(self.driver)
        return find_usps_location


