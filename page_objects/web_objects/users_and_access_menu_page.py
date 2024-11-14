from selenium.webdriver.common.by import By

users_and_access_page = (By.XPATH, "//a[@href='/admin/access']")
users_page = (By.XPATH, "//a[@href='/admin/users']")
teams_page = (By.XPATH, "//a[@href='/org/teams']")
service_accounts_page = (By.XPATH, "//a[@href='/org/serviceaccounts']")




class UserAndAccessMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_users_and_access_page(self):
        return self.driver.find_element(users_and_access_page[0], users_and_access_page[1])

    def get_users_page(self):
        return self.driver.find_element(users_page[0], users_page[1])

    def get_teams_page(self):
        return self.driver.find_element(teams_page[0], teams_page[1])

    def get_service_accounts_page(self):
        return self.driver.find_element(service_accounts_page[0], service_accounts_page[1])