import test_cases.conftest
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.upper_menu_page import UpperMenuPage
from page_objects.web_objects.users_and_access_menu_page import UserAndAccessMenuPage
from page_objects.web_objects.administration_menu_page import AdministrationMenuPage
from page_objects.web_objects.left_menu_page import LeftMenuPage
from page_objects.web_objects.new_user_page import NewUserPage
from page_objects.web_objects.user_information_page import UserInformationPage
from page_objects.web_objects.users_page import UsersPage

# Web Objects
web_login = None
web_main = None
web_upper_menu = None
web_left_menu = None
web_administration_menu = None
web_user_and_access_menu = None
web_users = None
web_new_user = None
web_users_information = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(test_cases.conftest.driver)
        globals()['web_main'] = MainPage(test_cases.conftest.driver)
        globals()['web_upper_menu'] = UpperMenuPage(test_cases.conftest.driver)
        globals()['web_left_menu'] = LeftMenuPage(test_cases.conftest.driver)
        globals()['web_administration_menu'] = AdministrationMenuPage(test_cases.conftest.driver)
        globals()['web_user_and_access_menu'] = UserAndAccessMenuPage(test_cases.conftest.driver)
        globals()['web_users'] = UsersPage(test_cases.conftest.driver)
        globals()['web_new_user'] = NewUserPage(test_cases.conftest.driver)
        globals()['web_users_information'] = UserInformationPage(test_cases.conftest.driver)



