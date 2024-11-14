from selenium.webdriver.common.by import By

name  = (By.ID, "name-input")
email = (By.ID, "email-input")
username = (By.ID, "username-input")
password = (By.ID, "password-input")
create_user_button = (By.CLASS_NAME, "css-td06pi-button")




class NewUserPage:
    def __init__(self, driver):
        self.driver = driver

    def get_name(self):
        return self.driver.find_element(name[0], name[1])

    def get_email(self):
        return self.driver.find_element(email[0], email[1])

    def get_username(self):
        return self.driver.find_element(username[0], username[1])

    def get_password(self):
        return self.driver.find_element(password[0], password[1])

    def get_create_user_button(self):
        return self.driver.find_element(create_user_button[0], create_user_button[1])