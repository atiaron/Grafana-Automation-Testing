from selenium.webdriver.common.by import By

search = (By.CLASS_NAME, "css-8tk2dk-input-input")
new_user_button = (By.CLASS_NAME, "css-td06pi-button")
users_list = (By.XPATH, "//table[@class='css-elscwy']/tbody/tr")
user_by_index = (By.CLASS_NAME, "css-1qmcwme")
user_by_user_name = (By.XPATH, "//a[@title='Edit user' and text()='replace_this_name']")




class UsersPage:
    def __init__(self, driver):
        self.driver = driver

    def get_search(self):
        return self.driver.find_element(search[0], search[1])

    def get_new_user_button(self):
        return self.driver.find_element(new_user_button[0], new_user_button[1])


    def get_users_list(self):
        return self.driver.find_elements(users_list[0], users_list[1])

    def get_user_by_index(self, index):
        user_row = self.get_users_list()[index]
        return user_row.find_element(user_by_index[0], user_by_index[1])


    def get_user_by_user_name(self, user: str):
        return self.driver.find_element(user_by_user_name[0], user_by_user_name[1].replace('replace_this_name', user))
