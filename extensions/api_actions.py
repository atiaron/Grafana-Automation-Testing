import allure
import requests
from requests.auth import HTTPBasicAuth

header = {'Content-Type': 'application/json'}

class APIAction:
    @staticmethod
    @allure.step('Get Request')
    def get(path, user, password):
        response = requests.get(path, auth=HTTPBasicAuth(user, password))
        return response

    @staticmethod
    @allure.step('Extract Value from response')
    def extract_value_value_from_response(response, nodes):
        extracted_json = None
        response_json = response.json()
        if len(nodes) == 1:
            extracted_json = response_json[nodes[0]]
        elif len(nodes) == 2:
            extracted_json = response_json[(nodes[0])][(nodes[1])]
        else:
            extracted_json = response_json[(nodes[0])][(nodes[1])][(nodes[2])]
        return extracted_json

    @staticmethod
    @allure.step('POST Request')
    def post(path, payload, user, password):
        response = requests.post(path, json=payload, headers=header, auth=HTTPBasicAuth(user, password))
        return response.status_code

    @staticmethod
    @allure.step('PUT Request')
    def put(path, payload, user, password):
        response = requests.put(path, json=payload, headers=header, auth=HTTPBasicAuth(user, password))
        return response.status_code

    @staticmethod
    @allure.step('DELETE Request')
    def delete(path, user, password):
        response = requests.delete(path, auth=HTTPBasicAuth(user, password))
        return response.status_code





