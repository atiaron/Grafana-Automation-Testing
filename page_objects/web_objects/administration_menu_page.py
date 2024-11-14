from selenium.webdriver.common.by import By

administration_page = (By.CSS_SELECTOR, "a[href='/admin']")
general_menu = (By.XPATH, "//button[@aria-label='Expand section General']")
plugins_and_data_menu = (By.XPATH, "//button[@aria-label='Expand section Plugins and data']")
users_and_access_open_menu = (By.XPATH, "//button[@aria-label='Expand section Users and access']")
authentication_page = (By.XPATH, "//a[@href='/admin/authentication']")
users_and_access_close_menu = (By.XPATH, "//button[@aria-label='Collapse section Users and access']")


class AdministrationMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_administration_page(self):
        return self.driver.find_element(administration_page[0], administration_page[1])

    def get_general_menu(self):
        return self.driver.find_element(general_menu[0], general_menu[1])


    def get_plugins_and_data_menu(self):
        return self.driver.find_element(plugins_and_data_menu[0], plugins_and_data_menu[1])

    def get_users_and_access_open_menu(self):
        return self.driver.find_element(users_and_access_open_menu[0], users_and_access_open_menu[1])

    def get_users_and_access_close_menu(self):
        return self.driver.find_element(users_and_access_close_menu[0], users_and_access_close_menu[1])

    def get_authentication_page(self):
        return self.driver.find_element(authentication_page[0], authentication_page[1])

