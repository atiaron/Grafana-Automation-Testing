import allure
from applitools.selenium import Eyes
from selenium.webdriver import ActionChains
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None
action = None
eyes = Eyes()  # כאן אנו מאתחלים את אובייקט ה-Eyes



@pytest.fixture(scope='class')
def init_web_driver(request):
    if get_data('Execute_Applitools').lower() == 'yes':
        # אם Execute_Applitools הוא 'yes', נשתמש ב-Applitools
        globals()['driver'] = get_web_driver()
        # הגדרת ה-API Key של Applitools
    else:
        # אחרת, נשתמש ב-EventFiringWebDriver כרגיל
        edriver = get_web_driver()
        globals()['driver'] = EventFiringWebDriver(edriver, EventListener())

    driver = globals()['driver']
    # הגדרות נוספות לדרייבר
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(int(get_data('wait_time')))
    driver.get(get_data('url'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()

    # אם השתמשנו ב-Applitools, נסגור את ה-eyes בסיום
    if get_data('Execute_Applitools').lower() == 'yes':
        eyes.api_key = get_data('Applitools_Key')
    yield
    driver.quit()
    if get_data('Execute_Applitools').lower() == 'yes':
        eyes.close() # applitools
        eyes.abort() # applitools


def get_web_driver():
    web_driver = get_data('browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception("wrong input")
    return driver


def get_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def get_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return driver


def get_edge():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return driver


def pytest_exception_interact(node, call, report):
    if report.failed:  # אם הטסט נכשל
        if globals()['driver'] is not None: # if it is None -> this is exception from API test
            image = get_data('screenshots_path') + 'screen_' + str(get_time_stamp()) + '.png'  # נגדיר נתיב ושם לתמונה
            globals()['driver'].get_screenshot_as_file(image)  # נבצע צילום מסך
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)  # נוסיף את התמונה לדוח Allure
