import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
 
appium_service = AppiumService()
appium_service.start()
caps = {
  "appPackage": "com.bettervet",
  "appActivity": "com.bettervet.MainActivity",
  "platformName": "Android",
  "deviceName": "Samsung Galaxy S21",
  "udid": "emulator-5554"
}
desired_caps = {} 
desired_caps['platformName'] = 'Android' 
# desired_caps['platformVersion'] = '12'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'Samsung Galaxy S21' 
desired_caps['app'] = ('/Users/jcgularte/Downloads/BetterVet-QA.apk') 
# desired_caps['appPackage'] = 'com.bettervet' 
# desired_caps['appActivity'] = 'com.bettervet.MainActivity'
desired_caps['browserName'] = 'Chrome'
# desired_caps['fullReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print("Check Whether device is locked or not :",driver.is_locked())
print("Current Activity",driver.current_package)
print("Current Activity",driver.current_activity)
print("Current context",driver.current_context)
print("Current orientation",driver.orientation)

driver.get("https://uat.parking.com")
driver.save_screenshot()

# waitToBeClickable = WebDriverWait(driver,15).until(EC.element_to_be_clickable(locator))
login_link_locator = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Login")')
email_input_locator = AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.EditText"
pwd_input_locator = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.EditText")
login_button_locator = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]")
# bettervet_initial_loader = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup")
wait = WebDriverWait(driver,15,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
# login_link = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Login")')).click()
wait.until(lambda  x: x.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"))
time.sleep(6)
login_link = wait.until(EC.element_to_be_clickable(login_link_locator))
# print(login_link.text)
login_link.click()

email_input = wait.until(EC.visibility_of_element_located(email_input_locator))
pwd_input = wait.until(EC.visibility_of_element_located(pwd_input_locator))
login_button = wait.until(EC.element_to_be_clickable(login_button_locator))
# print(login_link.text)

email_input.send_keys('juancarlosgularte@bettervet.com')
pwd_input.send_keys("Helloworld10")
login_button.click()

print("USER LOGGED IN")

# deviceSize = driver.get_window_size()
# screenWidth = deviceSize['width']
# screenHeight = deviceSize['height']
# ######Right to Left#######
# startx = screenWidth*8/9
# endx = screenWidth/9
# starty = screenHeight/2
# endy = screenHeight/2
# ###### Left to Right #######
# startx2 = screenWidth/9
# endx2 = screenWidth*8/9
# starty2 = screenHeight/2
# endy2 = screenHeight/2
actions = ActionChains(driver)
wait.until_not(lambda  x: x.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView"))
wait.until(lambda  x: x.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup"))
driver.swipe(970, 600, 30, 600)
# actions.click_and_hold(None,970,600).move_to(None,30,600).release().perform()

referral_box = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(text("Give $100, Get $100"))'))
referral_box.click()
# driver.quit()
# appium_service.stop()