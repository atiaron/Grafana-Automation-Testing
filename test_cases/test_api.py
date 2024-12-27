import allure

from api_flows import APIFLows
from verifications import Verifications

team_name = 'Ron'
team_email = 'ron@gmail.com'

class Test_API:
    @allure.title('Test01: Create Team & Verify status code')
    @allure.description('this test creates new team in  grafana')
    def test_create_and_verify_team(self):
        actual = APIFLows.create_team(team_name, team_email)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test02: Verify Team Name')
    @allure.description('this test verifies the grafana team member name')
    def test_verify_team_member_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFLows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name)

    @allure.title('Test03: Update team & Verify Status Code')
    @allure.description('this test update team & Verify status Code')
    def test_update_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFLows.get_value_from_api(nodes)
        actual = APIFLows.update(team_name + ' Goshen', team_email, id)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test04: Update Team Nmae')
    @allure.description('this test verifies team member name')
    def test_verify_team_updated_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFLows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name + ' Goshen')

    @allure.title('Test05: Delete Team & Verify Status Code')
    @allure.description('this test team and verify status code')
    def test_delete_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFLows.get_value_from_api(nodes)
        actual = APIFLows.delete_team(id)
        Verifications.verify_equals(actual, 200)