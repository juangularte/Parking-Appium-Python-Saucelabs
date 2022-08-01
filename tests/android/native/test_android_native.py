from ast import Assert
import unittest
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
import src.helpers.CustomLogger as cl
from src.screens.android.native.Welcome_Screen.welcome_screen_actions import WelcomeScreenActions

class TestAndroidNative():
    
    @pytest.mark.AndroidNative
    @pytest.mark.usefixtures("init_driver")
    def test_methodOne(self):
        log = cl.customLogger()
        welcome = WelcomeScreenActions(self.driver)

        elementLocator = (AppiumBy.ID, "com.spplus.parking.develop:id/text1")
        elementLocated = WebDriverWait(self.driver,15).until(EC.presence_of_element_located(elementLocator)).text
        # text = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[1]").text
        assert elementLocated == "Easily book daily and monthly parking when you need it."

        welcome.Welcome_screen_basic_assertions()
        cl.allureLogs("Welcome screen texts were correctly asserted.")
        welcome.clickOnLetsParkButton()
        cl.allureLogs("Let's Park button was clicked.")

        log.info("Assertion passed.")
        self.driver.execute_script('sauce:job-result=passed')


    @pytest.mark.AndroidNative
    @pytest.mark.usefixtures("init_driver")
    def test_methodTwo(self):
        log = cl.customLogger()
        welcome = WelcomeScreenActions(self.driver)

        try:
            welcome.Welcome_screen_basic_assertions()
            assert 1+1 == 3
            self.driver.execute_script('sauce:job-result=passed')
        except AssertionError as e:
            self.driver.save_screenshot("output/screenshots/error.png")
            log.error("Assertion error")
            self.driver.execute_script('sauce:job-result=failed')
            pytest.fail(str(e))
            
            # m2.critical("Critical Msg")
            # m2.warning("Warn msg")
            # m2.info("Info msg")
            # m2.debug("Debug msg")

# test =Test()
# test.methodOne()
# test.methodTwo()

