from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from selenium.webdriver.common.keys import Keys

class InitDriver:

    def __init__(self, device):
        self.device = device

    # @pytest.mark.parametrize("platform, version, device, app", 
    # [
    #     ("Android", "12", "Google Pixel 6 GoogleAPI Emulator", "storage:filename=app-uat-release.apk"),
    #     ("Android", "11", "Samsung Galaxy S20 WQHD GoogleAPI Emulator", "storage:filename=app-uat-release.apk")
    # ])
    def createDriverSession(self):

        local_url = "http://127.0.0.1:4723/wd/hub"
        saucelabs_url = "https://@ondemand.us-west-1.saucelabs.com:443/wd/hub"
        sauce_username = "jcgularte"
        sauce_access_key = "636020b5-5aea-420c-8d29-01d7b96233db"

        if self.device == "android":

            android_native_caps = {} 
            android_native_caps['platformName'] = 'android' 
            android_native_caps['platformVersion'] = '12'
            android_native_caps['automationName'] = 'UiAutomator2'
            android_native_caps['deviceName'] = 'Samsung Galaxy S21'
            # android_native_caps['udid'] = 'emulator-5554'
            # android_native_caps['systemPort'] = '8200'
            android_native_caps['app'] = ('/Users/juan.gularte/Desktop/Repositories/Python-Appium-Android-iOS/src/apps/parking-test.apk')
            android_native_caps['appPackage'] = 'com.spplus.parking.develop' 
            android_native_caps['appActivity'] = 'com.spplus.parking.presentation.splash.SplashActivity' 

            driver = webdriver.Remote(local_url, android_native_caps)
            print("Check Whether device is locked or not :",driver.is_locked())
            print("Current Activity",driver.current_package)
            print("Current Activity",driver.current_activity)
            print("Current context",driver.current_context)
            print("Current orientation",driver.orientation)

        elif self.device == "ios":

            ios_native_caps = {} 
            ios_native_caps['platformName'] = 'IOS' 
            ios_native_caps['platformVersion'] = '15.5'
            ios_native_caps['automationName'] = 'XCUITest'
            ios_native_caps['deviceName'] = 'iPhone 13 Pro Max'
            ios_native_caps['autoAcceptAlerts'] = 'true'
            ios_native_caps['app'] = '/Users/jcgularte/Desktop/Cursos/Repositories/Java-Appium-Android-iOS/src/main/resources/BetterVet.app'
            ios_native_caps['useNewWDA'] = 'true'

            driver = webdriver.Remote(local_url, ios_native_caps)
            driver.implicitly_wait(6)

        elif self.device == "android-saucelabs":
            saucelabs_android_caps = {}
            saucelabs_android_caps['platformName'] = 'Android'
            saucelabs_android_caps['appium:app'] = 'storage:filename=app-uat-release.apk' # The filename of the mobile app
            saucelabs_android_caps['appium:deviceName'] = 'Google Pixel 6 Pro GoogleAPI Emulator'
            saucelabs_android_caps['appium:platformVersion'] = '12.0'
            saucelabs_android_caps['sauce:options'] = {}
            saucelabs_android_caps['sauce:options']['appiumVersion'] = '1.22.1'
            saucelabs_android_caps['sauce:options']['username'] = sauce_username
            saucelabs_android_caps['sauce:options']['accessKey'] = sauce_access_key
            # caps['sauce:options']['build'] = '<your build id>'
            saucelabs_android_caps['sauce:options']['name'] = 'Android Execution'

            driver = webdriver.Remote(saucelabs_url, saucelabs_android_caps)
        
        elif self.device == "ios-saucelabs":
            saucelabs_ios_caps = {}
            saucelabs_ios_caps['platformName'] = 'iOS'
            saucelabs_ios_caps['appium:app'] = 'storage:filename=Parking Dev.ipa' # The filename of the mobile app
            saucelabs_ios_caps['appium:deviceName'] = 'iPhone 13 Simulator'
            saucelabs_ios_caps['appium:platformVersion'] = '15.4'
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

            driver = webdriver.Remote(local_url, ios_hybrid_caps)
            driver.get("https://uat.parking.com")

        elif self.device == "android-hybrid":

            android_hybrid_caps = {} 
            android_hybrid_caps['platformName'] = 'Android'
            android_hybrid_caps['automationName'] = 'UiAutomator2'
            android_hybrid_caps['deviceName'] = 'Samsung S22 API 31'
            android_hybrid_caps['browserName'] = 'Chrome'

            driver = webdriver.Remote(local_url, android_hybrid_caps)
            driver.get("https://uat.parking.com")

            print("Check Whether device is locked or not :",driver.is_locked())
            print("Current Activity",driver.current_package)
            print("Current Activity",driver.current_activity)
            print("Current context",driver.current_context)
            print("Current orientation",driver.orientation)

        else:
            print("No device found for the option you have chosen. Please choose an option between 'ios', 'android', 'ios-hybrid' or 'android-hybrid'.")

        return driver
