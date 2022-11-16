import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import src.helpers.CustomLogger as cl

class Test():

    @pytest.mark.AndroidHybrid
    @pytest.mark.usefixtures("init_driver")
    def test_methodOne(self):
        log = cl.customLogger()
        text = self.driver.find_element(AppiumBy.XPATH, "//p[@class='mt-lg-3 m-0 mt-2']").text
        assert text == "Finding parking shouldn’t be a hassle."
        log.info("Assertion passed.")

    @pytest.mark.AndroidHybrid
    @pytest.mark.usefixtures("init_driver")
    def test_methodTwo(self):
        log = cl.customLogger()
        text = self.driver.find_element(AppiumBy.XPATH, "//p[@class='mt-lg-3 m-0 mt-2']").text
        try:
            assert text == "Finding parking shouldn’t be a hassle", "TEXTS ARE NOT EQUAL"
        except AssertionError as e:
            log.error("Assertion error")
            pytest.fail(str(e))
            # m2.critical("Critical Msg")
            # m2.warning("Warn msg")
            # m2.info("Info msg")
            # m2.debug("Debug msg")

# test =Test()
# test.methodOne()
# test.methodTwo()

