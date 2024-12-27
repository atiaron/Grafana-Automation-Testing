from selenium.webdriver.common.by import By

ueser_name = (By.NAME, "user")
password = (By.NAME, "password")
Log_in_button = (By.CLASS_NAME, "css-1b7vft8-button")
skip_button = (By.CLASS_NAME, "css-bhnz0e-button")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(ueser_name[0], ueser_name[1])

    def get_password(self):
        return self.driver.find_element(password[0], password[1])

    def get_log_in_button(self):
        return self.driver.find_element(Log_in_button[0], Log_in_button[1])

    def get_skip_button(self):
        return self.driver.find_element(skip_button[0], skip_button[1])
