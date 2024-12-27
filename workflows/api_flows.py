
import allure

from api_actions import APIAction
from common_ops import get_data

url = get_data('url')
username = get_data('username')
password =get_data('password')


class APIFLows:
    @staticmethod
    @allure.step('Get Value from grafana api flow')
    def get_value_from_api(nodes):
        response = APIAction.get(url + 'api/teams/search', username, password)
        return APIAction.extract_value_value_from_response(response, nodes)

    @staticmethod
    @allure.step('Get Create new team in grafana flow')
    def create_team(name, email):
        peyload = {'name': name, 'email': email}
        status_code = APIAction.post(url + 'api/teams/', peyload, username, password)
        return status_code

    @staticmethod
    @allure.step('Update team in grafana flow')
    def update(name, email, id):
        peyload = {'name': name, 'email': email}
        status_code = APIAction.put(url + 'api/teams/' + str(id), peyload, username, password)
        return status_code

    @staticmethod
    @allure.step('Delete team in grafana flow')
    def delete_team(id):
        status_code = APIAction.delete(url + 'api/teams/' + str(id), username, password)
        return status_code
