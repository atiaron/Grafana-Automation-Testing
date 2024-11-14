from selenium.webdriver.common.by import By

delete_user_button = (By.XPATH, "//div/button[@class='css-ttl745-button']")
confirm_delete_button = (By.XPATH, "//button[@data-testid='data-testid Confirm Modal Danger Button']")





class UserInformationPage:
    def __init__(self, driver):
        self.driver = driver

    def get_delete_user_button(self):
        return self.driver.find_element(delete_user_button[0], delete_user_button[1])

    def get_confirm_delete_button(self):
        return self.driver.find_element(confirm_delete_button[0], confirm_delete_button[1])