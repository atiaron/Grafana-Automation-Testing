import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step("Verifying if Actual Value Equals Expected")
    def verify_equals(actual, expected):
        assert actual == expected, 'Verify Equals Failed: ' + str(actual) + ' is not Equals to Expected: ' + str(expected)


    @staticmethod
    @allure.step("Asserting if the Element Is Displayed")
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), 'Verify is Displayed Failed: ' + elem.text + ' is not Displayed: '


    # verify menu buttons using smart assertions
    @staticmethod
    @allure.step("Soft Asserting Elements Are Displayed")
    def soft_assert_elements_displayed(elems):
        for elem in range(len(elems)):
            soft_assert(elems[elem].is_displayed())
            verify_expectations()


    # verify menu buttons using my implementation
    @staticmethod
    @allure.step("Soft Asserting Elements Are Displayed Using Custom Implementation")
    def soft_displayed(elems):
        failed_elements = []
        for elem in elems:
            if elem.is_displayed():
                pass
            else:
                failed_elements.append(elem.get_attribute('aria-label'))
        if len(failed_elements) > 0:
            for elem in failed_elements:
                print('soft displayed error: ' + str(elem) + ' ' 'is not displayed')
            raise AttributeError('Soft Displayed Error')

    @staticmethod
    @allure.step("Verifying Number of Users Matches Expected Value")
    def assert_number_of_users(elems, size):
            assert len(elems) == size, 'Number of user in list: ' + str(elems) + 'does not match expected: ' + str(size)



