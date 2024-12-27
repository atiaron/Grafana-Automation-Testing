import csv
import time
import xml.etree.ElementTree as ET
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_cases.conftest

def get_data(node_name):
    tree = ET.parse(r'c:\Users\moshiach\Automation\test_automation_final_project\configuration\data.xml')
    root = tree.getroot()
    return root.find('.//' + node_name).text


def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
        return data

def get_time_stamp():
    return time.time()  # נחזיר את הזמן הנוכחי בפורמט מספרי

def wait(wait_type, elem):
    if wait_type == 'element_exists':
        WebDriverWait(test_cases.conftest.driver, int(get_data('wait_time'))).until(expected_conditions.presence_of_element_located((elem[0], elem[1])))
    elif wait_type == 'element_displayed':
        WebDriverWait(test_cases.conftest.driver, int(get_data('wait_time'))).until(expected_conditions.visibility_of_element_located((elem[0], elem[1])))





class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'

class By:
    NAME = 'name'
    INDEX = 'index'