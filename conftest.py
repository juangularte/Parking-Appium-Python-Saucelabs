import pytest
from appium import webdriver
import allure
from src.base.Driver import InitDriver

desired_caps = {} 
desired_caps['platformName'] = 'ios' 
desired_caps['platformVersion'] = '15.5'
desired_caps['automationName'] = 'XCUITest'
desired_caps['deviceName'] = 'iPhone 13 Pro Max'
# desired_caps['app'] = ('/Users/jcgularte/Downloads/BetterVet-QA.apk') 
desired_caps['autoWebview'] = 'true' 
desired_caps['browserName'] = 'safari'
desired_caps['startIWDP'] = 'true'


@pytest.fixture()
def init_driver(request, device):

    device = InitDriver(device)
    driver = device.createDriverSession()
    request.cls.driver = driver
    
    with allure.step("LAUNCHING APP"):
        print("TEST HAS STARTED")
        yield
        print("TEST HAS FINISHED")
        driver.quit()

def pytest_addoption(parser): #method to add commands specifications
    parser.addoption("--device", help="Type of device to use for the execution.")
    # parser.addoption("--env", help="Environment where the tests will be executed.")

@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")

# @pytest.fixture(scope="session")
# def env(request):
#     return request.config.getoption("--env")

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_protocol(item, nextitem):
#     # reports = runtestprotocol(item, nextitem=nextitem)
#     # pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == 'call':
#         driver_fixture = item.funcargs["request"]
#         driver_fixture.cls.driver.execute_script('sauce:job-result={}'.format(report.outcome))
#     return True
