from appium.webdriver.common.appiumby import AppiumBy

class WelcomeScreenLocators():
    
    # loading_image = (By.CSS_SELECTOR, ".loadingIndicator__background")

    #Header
    logo = (AppiumBy.ID, "com.spplus.parking.develop:id/logo")
    slogan_1 = (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.spplus.parking.develop:id/subtitleLinearLayout']//android.widget.TextView[1]")
    slogan_2 = (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.spplus.parking.develop:id/subtitleLinearLayout']//android.widget.TextView[2]")
    slogan_3 = (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.spplus.parking.develop:id/subtitleLinearLayout']//android.widget.TextView[3]")
    easily_book = (AppiumBy.ID, "com.spplus.parking.develop:id/text1")
    monthly_parking = (AppiumBy.ID, "com.spplus.parking.develop:id/text2")
    event_parking = (AppiumBy.ID, "com.spplus.parking.develop:id/text3")
    help_us = (AppiumBy.ID, "com.spplus.parking.develop:id/helpUsTextView")
    location_permission_warning = (AppiumBy.ID, "com.spplus.parking.develop:id/locationAwareTextView")
    lets_park_button = (AppiumBy.ID, "com.spplus.parking.develop:id/letsParkButton")
    powered_by = (AppiumBy.XPATH, "//android.widget.TextView[@text='Powered by']")

    