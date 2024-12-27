from selenium.webdriver.support.events import AbstractEventListener


class EventListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print(f"[*] Before navigating to: {url}")

    def after_navigate_to(self, url, driver):
        print(f"[+] After navigating to: {url}")

    def before_find(self, by, value, driver):
        print(f"[*] Before finding element by {by} with value {value}")

    def after_find(self, by, value, driver):
        print(f"[+] After finding element by {by} with value {value}")

    def before_click(self, element, driver):
        print(f"[*] Before clicking on element: {element}")

    def after_click(self, element, driver):
        print(f"[+] After clicking on element: {element}")

    def before_change_value_of(self, element, driver):
        print(f"[*] Before changing value of element: {element}")

    def after_change_value_of(self, element, driver):
        print(f"[+] After changing value of element: {element}")
