import requests
from requests import Response
from streamlit import secrets


class Logos:
    def __init__(self):
        self.ngus_url = secrets['NGUS_URL']
        self.npi_url = secrets['NPI_URL']
        self.mw_ok = {'Authorization': f'Basic {secrets["MW_OK"]}'}
        self.always_data_url = secrets['ALWAYS_DATA_URL']
        self.top_stage_url = secrets['TOP_STAGE_URL']
        self.top_prod_url = secrets['TOP_PROD_URL']

    def iew_create(self, contour: str, body: dict) -> Response:
        url = {'ngus': self.ngus_url, 'npi': self.npi_url}
        response = requests.post(url[contour], json=body, headers=self.mw_ok)
        return response

    def read_iew(self, contour: str) -> Response:
        url = f'{self.always_data_url}/read/{contour}'
        response = requests.get(url)
        return response

    def write_iew(self, iew: str) -> Response:
        url = f'{self.always_data_url}/write'
        body = {'iew': iew}
        response = requests.post(url, json=body)
        return response
