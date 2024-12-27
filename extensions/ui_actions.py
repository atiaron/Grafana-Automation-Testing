import allure

import test_cases.conftest


class UiActions:
    @staticmethod
    @allure.step("Clicks on an Element")
    def click(elem):
        elem.click()

    @staticmethod
    @allure.step("Sends Text to an Element")
    def send_text(elem, value):
        elem.send_keys(value)


    @staticmethod
    @allure.step("Hovering Over and Clicking on Element")
    def mouse_over(element):
        test_cases.conftest.action.move_to_element(element).click().perform()


    @staticmethod
    @allure.step("Hovering Over Element")
    def mouse_hover1(elem3):
        test_cases.conftest.action.move_to_element(elem3).perform()

    @staticmethod
    @allure.step("Right-Clicking on Element")
    def right_click(elem):
        test_cases.conftest.action.context_click(elem).perform()

    @staticmethod
    @allure.step("Clearing the Element's Content")
    def clear(elem):
        elem.clear()



