from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BaseMethods:

    def __init__(self,driver):
        self.driver = driver
        self.default_timeout=15

    def findElement(self, locator, timeout=None):
        try:
            timeout = timeout if timeout else self.default_timeout
            elementLocated = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
                                                                    #,message=f"Cannot find the element {locator}.")
            # self.allure_screenshot("ELEMENT FOUND")
            return elementLocated
        except:
            pytest.fail(f"Cannot find the element {locator}.")

    def find_iframe(self, locator, timeout=None):
        try:
            timeout = timeout if timeout else self.default_timeout
            elementLocated = WebDriverWait(self.driver,200).until(EC.frame_to_be_available_and_switch_to_it(locator))
                                                                    #,message=f"Cannot find the element {locator}.")
            return elementLocated
        except TimeoutException as e:
            assert False, f"Cannot find the element {locator}."

    def findElementIframe(self, locator, timeout=None):
        try:
            timeout = timeout if timeout else self.default_timeout
            elementLocated = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
                                                                    #,message=f"Cannot find the element {locator}.")
            return elementLocated
        except TimeoutException as e:
            assert False, f"Cannot find the element {locator}."

    def element_not_present(self, locator):
        try:
            element_not_found = WebDriverWait(self.driver, 1).until_not(EC.presence_of_element_located(locator))
            return element_not_found
        except TimeoutException as e:
            assert False, f"Cannot find the element {locator}."
        except AttributeError as e:
            assert False, f"Cannot click the element {locator}. {e}"

    def find_clickable_element(self, locator, timeout=None):
        try:
            timeout = timeout if timeout else self.default_timeout
            elementLocated = WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))
            return elementLocated
        except:
            pytest.fail(f"Cannot find the element {locator}.")
        
    def wait_for_element_to_disappear(self, locator):
        WebDriverWait(self.driver,15000).until_not(EC.presence_of_element_located(locator))

    def check_element_is_present(self, locator):
        try:
            element = self.driver.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def go_to_url(self, url):
        self.driver.get(url)

    def sleep(self, seconds):
        self.driver.implicitly_wait(seconds)

    # def try_assertion(self, locator, text):
    #     try:
    #         self.assert_text(locator, text)
    #     except:
    #         print(f"Text Expected: {self.get_text(locator)}  \
    #             Text entered: {text}")

    def text_input(self, locator, text):
        self.findElement(locator).send_keys(Keys.COMMAND + "a")
        self.findElement(locator).send_keys(Keys.DELETE)
        self.findElement(locator).send_keys(text)

    def text_input_iframe(self, locator, text):
        # self.findElementIframe(locator).send_keys(Keys.COMMAND + "a")
        # self.findElementIframe(locator).send_keys(Keys.DELETE)
        self.findElementIframe(locator).send_keys(text)

    def clear_input(self, locator):
        self.findElement(locator).send_keys(Keys.COMMAND + "a")
        self.findElement(locator).send_keys(Keys.DELETE)

    def text_and_enter(self, locator, text):
        self.findElement(locator).clear()
        self.findElement(locator).send_keys(text, Keys.ENTER)

    def click_element (self, locator):
        self.find_clickable_element(locator).click()

    def get_text (self, locator):
        return self.findElement(locator).text

    def split_text(self, locator):
        return self.get_text(locator).split()

    def get_input_value(self, locator):
        return self.get_attribute_of_element(locator, "value")

    def assert_input_value(self, locator, text):
        input_value = self.get_input_value(locator)
        assert input_value.upper().rstrip().lstrip() == text.upper(), f"Assertion failed. \
            \Value expected: \n'{input_value.upper().rstrip().lstrip()}' \
            \Value entered: \n'{text.upper()}'"

    def assert_text (self, locator, text):
        textOfElement=self.get_text(locator)
        assert textOfElement.upper().rstrip().lstrip() == text.upper(), f"Assertion failed. \
            \nText expected: \n'{textOfElement.upper().rstrip().lstrip()}' \
            \nText entered: \n'{text.upper()}'"

    def get_css_of_element (self, locator, property):
        return self.findElement(locator).value_of_css_property(property)
    
    def get_attribute_of_element (self, locator, attr):
        return self.findElement(locator).get_attribute(attr)
    
    def attribute_assertion (self, locator, attr, attrValue):
        valueObtained = self.get_attribute_of_element(locator,attr)
        assert valueObtained.upper().rstrip().lstrip() == attrValue.upper()
        return True
        
    def findElements(self, locator, timeout=None):
        try:
            timeout = timeout if timeout else self.default_timeout
            elementsLocated = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
            return elementsLocated
        except TimeoutException as e:
            assert False, f"Cannot find the element {locator}."

    def find_element_in_elements_list(self,locator, option):
        elements = self.findElements(locator)
        return elements[option]

    def click_element_from_list (self, locator, option):
        self.find_element_in_elements_list(locator,option).click()
    
    def get_text_of_element_in_elements_list(self,locator,option):
        return self.find_element_in_elements_list(locator,option).text

    def assert_text_of_element_in_elements_list(self, locator, option, text):
        textOfElement = self.get_text_of_element_in_elements_list(locator,option)
        assert textOfElement.upper().rstrip().lstrip() == text.upper(), f"Assertion failed. \
            \nText expected: \n'{textOfElement.upper().rstrip().lstrip()}' \
            \nText entered: \n'{text.upper()}'"

    def assert_there_is_one_element(self, locator):
        list = self.findElements(locator)
        assert len(list) == 1, f"There are more than one element: {locator}"

    def assert_same_text_in_elements_list(self, locator, text):
        list = self.findElements(locator)
        for i in range (0, len(list)):
            value = self.get_text_of_element_in_elements_list(locator, i)
            # print("TEXT OF POSITION "+str(i)+ " IS: "+value)
            assert value == text, f"The text '{text}' was not found in the element '{locator}' nº {i}"

    def allure_screenshot(self, name):
        allure.attach(self.driver.get_screenshot_as_png(), name= name, attachment_type= allure.attachment_type.PNG)

    # def find_child_in_element_from_elements_list(self, parentLocator, option, childLocator, text):
    #     elementFound = self.find_element_in_elements_list(parentLocator,option)
    #     textOfElement = elementFound.find_element(childLocator).text
    #     assert textOfElement.upper().rstrip().lstrip() == text.upper()

