import time
import allure
import page_objects.web_objects.main_page
import utilities.manage_pages as page
from utilities.common_ops import get_data, read_csv
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from utilities.common_ops import wait, For
import page_objects.web_objects.users_page


class WebFlow:
    @staticmethod
    @allure.step("Login to Grafana with username: {username} and password: {password}")
    def login_flow(username, password):
        UiActions.send_text(page.web_login.get_user_name(), username)
        UiActions.send_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_log_in_button())
        UiActions.click(page.web_login.get_skip_button())

    @staticmethod
    @allure.step("Verifiy Title after Login")
    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_EXISTS, page_objects.web_objects.main_page.page_title)
        actual = page.web_main.get_page_title().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step("Verifiy Elements are Displayed in the top menu on the Home Page")
    def verify_menu_button_exists():
        elems = [page.web_upper_menu.get_new(),
                 page.web_upper_menu.get_help(),
                 page.web_upper_menu.get_news(),
                 page.web_upper_menu.get_profile()]
        Verifications.soft_assert_elements_displayed(elems)

    @staticmethod
    @allure.step("Clicking on the left Menus and reaching the users page")
    def open_users_page():
        UiActions.click(page.web_left_menu.get_administration_open_menu())
        UiActions.click(page.web_administration_menu.get_users_and_access_open_menu())
        UiActions.click(page.web_user_and_access_menu.get_users_page())

    @staticmethod
    @allure.step("Create a New User")
    def create_user(name, email, username, password):
        UiActions.click(page.web_users.get_new_user_button())
        UiActions.send_text(page.web_new_user.get_name(), name)
        UiActions.send_text(page.web_new_user.get_email(), email)
        UiActions.send_text(page.web_new_user.get_username(), username)
        UiActions.send_text(page.web_new_user.get_password(), password)
        UiActions.click(page.web_new_user.get_create_user_button())
        UiActions.click(page.web_user_and_access_menu.get_users_page())

    @staticmethod
    @allure.step("Waiting for User List to Update")
    def wait_for_row_filter_change(expected_number):
        max_iterations = 2  # מספר הפעמים שהלולאה תרוץ
        iterations = 0
        while iterations < max_iterations:
            rows = page.web_users.get_users_list()  #כאן אנחנו מקבלים את השורות הנוכחיות
            if len(rows) == int(expected_number):  # אם מספר השורות שווה למספר הצפוי
                print(f"הטבלה התעדכנה! הלולאה רצה {iterations + 1} פעמים.")
                break  # מפסיקים את הלולאה אם הכל תקין
            time.sleep(0.5)
            iterations += 1  # מגדילים את מספר הריצות
        else:
            print(f"הטבלה לא התעדכנה. הלולאה רצה {max_iterations} פעמים.")
            raise AssertionError("הטבלה לא התעדכנה בזמן!")


    @staticmethod
    @allure.step("Checking If the Number of Users Matches the Expected Count")
    def verify_expected_users_count(expected_number):
        if expected_number > 0:
            wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.users_page.users_list)
            Verifications.assert_number_of_users(page.web_users.get_users_list(), expected_number)

    @staticmethod
    @allure.step("Clears Search Box and Searches for a Specific User")
    def search_user(search_value):
        UiActions.clear(page.web_users.get_search())
        UiActions.send_text(page.web_users.get_search(), search_value)

    @staticmethod
    @allure.step("Filters User Table by Name or Index and Deletes the Selected User")
    def delete_user(by, value):
        if by == 'name':
            UiActions.click(page.web_users.get_user_by_user_name(value))
        elif by == 'index':
            UiActions.click(page.web_users.get_user_by_index(value))
        UiActions.click(page.web_users_information.get_delete_user_button())
        UiActions.click(page.web_users_information.get_confirm_delete_button())

    @staticmethod
    @allure.step("Returns to Home Page and Closes Open Left Menus if Necessary")
    def grafana_home(self):
        self.driver.get(get_data('url'))
        try:
            users_and_access_menu_button_is_open = page.web_administration_menu.get_users_and_access_close_menu()
            if users_and_access_menu_button_is_open.is_displayed():
                UiActions.click(users_and_access_menu_button_is_open)
        except:
            pass
        try:
            administration_menu_button_is_open = page.web_left_menu.get_administration_close_menu()
            if administration_menu_button_is_open.is_displayed():
                UiActions.click(administration_menu_button_is_open)
        except:
            pass


data = read_csv(get_data('csv_location'))
testdata = [
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1]),
    (data[3][0], data[3][1])
]