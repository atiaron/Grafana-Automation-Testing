from selenium.webdriver.common.by import By

get_new = (By.CSS_SELECTOR, "button[aria-label='New']")
get_help = (By.CSS_SELECTOR, "button[aria-label='Help']")
get_news = (By.CSS_SELECTOR, "button[aria-label='News']")
get_profile = (By.CSS_SELECTOR, "button[aria-label='Profile']")


class UpperMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_new(self):
        return self.driver.find_element(get_new[0], get_new[1])

    def get_help(self):
        return self.driver.find_element(get_help[0], get_help[1])

    def get_news(self):
        return self.driver.find_element(get_news[0], get_news[1])

    def get_profile(self):
        return self.driver.find_element(get_profile[0], get_profile[1])