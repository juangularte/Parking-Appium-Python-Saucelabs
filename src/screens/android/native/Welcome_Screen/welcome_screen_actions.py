from src.screens.android.native.Welcome_Screen.welcome_screen_locators import WelcomeScreenLocators
from src.base.Base import BaseMethods
import logging as log

class WelcomeScreenActions (WelcomeScreenLocators): #the class is the object that represents the page, and inherits the locators from another class

    def __init__(self, driver):
        self.driver = driver
        self.base = BaseMethods(self.driver)

    def Welcome_screen_basic_assertions(self):
        self.base.findElement(self.logo)
        # self.base.wait_for_element_to_disappear(self.loading_image)
        slogan_1_text = "PARK"
        slogan_2_text = "BETTER"
        slogan_3_text = "PERIOD"
        easily_book_text = "Easily book daily and monthly parking when you need it."
        monthly_parking_text = "Manage your monthly parking account and payment."
        event_parking_text = "Find event parking for your favorite locations."
        help_us_text = "Help us find you parking!"
        location_permission_warning_text = "Parking.com will ask you to grant location permission to assist in finding parking near you."
        powered_by_text = "Powered by"
        self.base.assert_text(self.slogan_1, slogan_1_text)
        self.base.assert_text(self.slogan_2, slogan_2_text)
        self.base.assert_text(self.slogan_3, slogan_3_text)
        self.base.assert_text(self.easily_book, easily_book_text)
        self.base.assert_text(self.monthly_parking, monthly_parking_text)
        self.base.assert_text(self.event_parking, event_parking_text)
        self.base.assert_text(self.help_us, help_us_text)
        self.base.assert_text(self.location_permission_warning, location_permission_warning_text)
        self.base.assert_text(self.powered_by, powered_by_text)
        log.info("All the texts in Welcome screen were asserted.")

    def Click_on_lets_park_button(self):
        self.base.click_element(self.lets_park_button)
        log.info("Let's Park button was clicked.")

    def Go_to_dashboard_screen(self):
        self.Click_on_lets_park_button()

    def Assert_texts_and_navigate_to_dashboard_screen(self):
        self.Welcome_screen_basic_assertions()
        self.Click_on_lets_park_button()
    