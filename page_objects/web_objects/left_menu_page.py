from selenium.webdriver.common.by import By

open_menu = (By.ID, "mega-menu-toggle")
Home = (By.CLASS_NAME, "css-1pjaw4h")
Starred_menu = (By.XPATH, "//button[aria-label='Expand section Starred']")
Dashboards_menu = (By.XPATH, "//button[aria-label='Expand section Dashboards']")
Explore_menu = (By.XPATH, "//button[aria-label='Expand section Explore']")
Alerting_menu = (By.XPATH, "//button[aria-label='Expand section Alerting']")
Connections_menu = (By.XPATH, "//button[aria-label='Expand section Connections']")
administration_open_menu = (By.XPATH, "//button[@aria-label='Expand section Administration']")
administration_close_menu = (By.XPATH, "//button[@aria-label='Collapse section Administration']")


class LeftMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_open_menu(self):
        return self.driver.find_element(open_menu[0], open_menu[1])

    def get_home(self):
        return self.driver.find_element(Home[0], Home[1])

    def get_starred_menu(self):
        return self.driver.find_element(Starred_menu[0], Starred_menu[1])

    def get_dashboards_menu(self):
        return self.driver.find_element(Dashboards_menu[0], Dashboards_menu[1])

    def get_explore_menu(self):
        return self.driver.find_element(Explore_menu[0], Explore_menu[1])

    def get_alerting_menu(self):
        return self.driver.find_element(Alerting_menu[0], Alerting_menu[1])

    def get_connections_menu(self):
        return self.driver.find_element(Connections_menu[0], Connections_menu[1])

    def get_administration_open_menu(self):
        return self.driver.find_element(administration_open_menu[0], administration_open_menu[1])

    def get_administration_close_menu(self):
        return self.driver.find_element(administration_close_menu[0], administration_close_menu[1])



