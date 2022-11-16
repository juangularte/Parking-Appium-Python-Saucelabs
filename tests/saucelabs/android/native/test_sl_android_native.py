import unittest
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from src.base.SauceLabsDriver import InitSession
import src.helpers.CustomLogger as cl
from src.screens.android.native.Welcome_Screen.welcome_screen_actions import WelcomeScreenActions

class TestAndroidNative():
    
    @pytest.mark.parametrize("platform, version, deviceName, app", 
    [
        ("Android", "12", "Google Pixel 6 GoogleAPI Emulator", "storage:filename=storage:filename=app-qa-release.apk"),
        ("Android", "11", "Samsung Galaxy S20 WQHD GoogleAPI Emulator", "storage:filename=storage:filename=app-qa-release.apk")
    ])
    @pytest.mark.SLAndroidNative1
    # @pytest.mark.usefixtures("init_driver")
    def test_methodOne(self, platform, version, deviceName, app):
        log = cl.customLogger()

        driver = InitSession("android-saucelabs").createSauceLabsDriverSession(platform, version, deviceName, app, __name__)
        welcome = WelcomeScreenActions(driver)

        elementLocator = (AppiumBy.ID, "com.spplus.parking.develop:id/text1")
        elementLocated = WebDriverWait(driver,15).until(EC.presence_of_element_located(elementLocator)).text
        # text = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[1]").text
        assert elementLocated == "Easily book daily and monthly parking when you need it."

        welcome.Assert_texts_and_navigate_to_dashboard_screen()
        cl.allureLogs("Welcome screen texts were correctly asserted.")

        log.info("Assertion passed.")
        driver.execute_script('sauce:job-result=passed')
        driver.quit()


    @pytest.mark.parametrize("platform, version, deviceName, app", 
    [
        ("Android", "12", "Google Pixel 6 GoogleAPI Emulator", "storage:filename=app-uat-release.apk"),
        ("Android", "11", "Samsung Galaxy S20 WQHD GoogleAPI Emulator", "storage:filename=app-uat-release.apk")
    ])
    @pytest.mark.SLAndroidNative2
    # @pytest.mark.usefixtures("init_driver")
    def test_methodTwo(self, platform, version, deviceName, app):
        log = cl.customLogger()

        driver = InitSession("android-saucelabs").createSauceLabsDriverSession(platform, version, deviceName, app, __name__)
        welcome = WelcomeScreenActions(driver)

        try:
            welcome.Go_to_dashboard_screen()
            assert 1+1 == 3
            driver.execute_script('sauce:job-result=passed')
            driver.quit()
        except AssertionError as e:
            driver.save_screenshot("output/screenshots/error.png")
            log.error("Assertion error")
            driver.execute_script('sauce:job-result=failed')
            driver.quit()
            pytest.fail(str(e))
            
            # m2.critical("Critical Msg")
            # m2.warning("Warn msg")
            # m2.info("Info msg")
            # m2.debug("Debug msg")

# test =Test()
# test.methodOne()
# test.methodTwo()

