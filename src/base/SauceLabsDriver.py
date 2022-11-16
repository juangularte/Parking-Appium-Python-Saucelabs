from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from selenium.webdriver.common.keys import Keys

class InitSession:

    def __init__(self, device):
        self.device = device

    def createSauceLabsDriverSession(self, platform, version, deviceName, app, executionName):
    # def createDriverSession(self):
        saucelabs_url = "https://@ondemand.us-west-1.saucelabs.com:443/wd/hub"
        sauce_username = "jcgularte"
        sauce_access_key = "636020b5-5aea-420c-8d29-01d7b96233db"

        if self.device == "android-saucelabs":
            saucelabs_android_caps = {}
            saucelabs_android_caps['platformName'] = platform
            saucelabs_android_caps['appium:app'] = app
            saucelabs_android_caps['appium:deviceName'] = deviceName
            saucelabs_android_caps['appium:platformVersion'] = version
            saucelabs_android_caps['sauce:options'] = {}
            saucelabs_android_caps['sauce:options']['appiumVersion'] = '1.22.1'
            saucelabs_android_caps['sauce:options']['username'] = sauce_username
            saucelabs_android_caps['sauce:options']['accessKey'] = sauce_access_key
            # caps['sauce:options']['build'] = '<your build id>'
            saucelabs_android_caps['sauce:options']['name'] = executionName
            saucelabs_android_caps['sauce:options']['tags'] = ["tag1", "tag2", "tag3"]

            driver = webdriver.Remote(saucelabs_url, saucelabs_android_caps)
        
        elif self.device == "ios-saucelabs":
            saucelabs_ios_caps = {}
            saucelabs_ios_caps['platformName'] = platform
            saucelabs_ios_caps['appium:app'] = app
            saucelabs_ios_caps['appium:deviceName'] = deviceName
            saucelabs_ios_caps['appium:platformVersion'] = version
            saucelabs_ios_caps['sauce:options'] = {}
            saucelabs_ios_caps['sauce:options']['appiumVersion'] = '1.22.3'
            # caps['sauce:options']['build'] = '<your build id>'
            saucelabs_ios_caps['sauce:options']['name'] = 'iOS Execution'

            driver = webdriver.Remote(saucelabs_url, saucelabs_ios_caps)

        elif self.device == "ios-hybrid":

            ios_hybrid_caps = {} 
            ios_hybrid_caps['platformName'] = 'ios' 
            ios_hybrid_caps['platformVersion'] = '15.5'
            ios_hybrid_caps['automationName'] = 'XCUITest'
            ios_hybrid_caps['deviceName'] = 'iPhone 13 Pro Max'
            # ios_hybrid_caps['app'] = ('/Users/jcgularte/Downloads/BetterVet-QA.apk') 
            ios_hybrid_caps['autoWebview'] = 'true' 
            ios_hybrid_caps['browserName'] = 'safari'

            driver = webdriver.Remote(saucelabs_url, ios_hybrid_caps)
            driver.get("https://uat.parking.com")

        elif self.device == "android-hybrid":

            android_hybrid_caps = {} 
            android_hybrid_caps['platformName'] = 'Android'
            android_hybrid_caps['automationName'] = 'UiAutomator2'
            android_hybrid_caps['deviceName'] = 'Samsung S22 API 31'
            android_hybrid_caps['browserName'] = 'Chrome'

            driver = webdriver.Remote(saucelabs_url, android_hybrid_caps)
            driver.get("https://uat.parking.com")

            print("Check Whether device is locked or not :",driver.is_locked())
            print("Current Activity",driver.current_package)
            print("Current Activity",driver.current_activity)
            print("Current context",driver.current_context)
            print("Current orientation",driver.orientation)

        else:
            print("No device found for the option you have chosen. Please choose an option between 'ios', 'android', 'ios-hybrid' or 'android-hybrid'.")

        return driver
