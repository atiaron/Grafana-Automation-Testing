from selenium.webdriver.common.by import By

page_title = (By.CLASS_NAME, "css-17tm80")
alerting_button_menu = (By.XPATH, "//*[@id='reactRoot']/div[1]/div/div/div/div/nav/div/div[1]/div[2]/ul/div[5]/li/div/div[1]/button")
alert_rules = (By.XPATH, "//*[@id='reactRoot']/div[1]/div/div/div/div/nav/div/div[1]/div[2]/ul/div[5]/li/ul/li[1]/div/div[2]/a/div/div/span")


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.find_element(page_title[0], page_title[1])

    def get_alerting_button_menu(self):
        return self.driver.find_element(alerting_button_menu[0], alerting_button_menu[1])

    def get_alert_rules(self):
        return self.driver.find_element(alert_rules[0], alert_rules[1])
