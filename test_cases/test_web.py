import allure
import pytest
from utilities.common_ops import get_data, By
from workflows import web_flows
from workflows.web_flows import WebFlow
import test_cases.conftest as conf


@pytest.mark.usefixtures("init_web_driver")
class TestWeb:
    @allure.title("Test 01: Verify Login to Grafana")
    @allure.description("This Test verifies a successful login to Grafana")
    def test_verify_login(self):
        WebFlow.login_flow(get_data('username'), get_data('password'))
        WebFlow.verify_grafana_title('Welcome to Grafana')

    @allure.title("Test 02: Verify Upper Menu Button")
    @allure.description("This Test verifies that the upper menu buttons are displayed")
    def test_verify_upper_menu(self):
        WebFlow.verify_menu_button_exists()

    @allure.title("Test 03: Verify_New_User")
    @allure.description("This Test verifies add New User to Users List")
    def test_verify_new_user(self):
        WebFlow.open_users_page()
        WebFlow.create_user('ron_test', 'ron@gmail', 'rongoshen_test', "123456")
        WebFlow.verify_expected_users_count(2)

    @allure.title("Test 04: Search Users From CSV")
    @allure.description("This Test Verifies Search Users From CSV And Checks Expected User Count")
    @pytest.mark.parametrize('search_value,expected_user', web_flows.testdata)
    def test_search_from_csv(self, search_value, expected_user):
        WebFlow.open_users_page()
        WebFlow.search_user(search_value)
        WebFlow.wait_for_row_filter_change(expected_user)
        WebFlow.verify_expected_users_count(int(expected_user))

    @allure.title("Test 05: Delete User")
    @allure.description("This Test Delete User And Checks Expected User Count")
    def test_delete_user(self):
        WebFlow.open_users_page()
        WebFlow.delete_user(By.NAME, 'rongoshen_test')
        WebFlow.verify_expected_users_count(1)

    @allure.title("Test 06: Visual Testing")
    @allure.description("This test verifies visually the users table.")
    @pytest.mark.skipif(get_data('Execute_Applitools').lower() == 'no', reason='Applitools is disabled.')
    def test_visual_verify_users_table(self):
        # פתיחת בדיקת Applitools
        conf.eyes.open(conf.driver, 'Grafana', 'Users Table Visual Test')

        # ביצוע לוגין
        WebFlow.login_flow(get_data('username'), get_data('password'))

        # ניווט לעמוד המשתמשים
        conf.driver.get("http://localhost:3000/admin/users")

        # בדיקה ויזואלית
        conf.eyes.check_window("Users Table")

        # סגירת הבדיקה נעשית ב-conftest.py לאחר הטסט

    def teardown_method(self):
        WebFlow.grafana_home(self)




