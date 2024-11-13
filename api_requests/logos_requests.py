import requests
from requests import Response
from streamlit import secrets
import toml

class Logos:
    def __init__(self):
        self.ngus_url = secrets['NGUS_URL']
        self.npi_url = secrets['NPI_URL']
        self.mw_ok = {'Authorization': f'Basic {secrets["MW_OK"]}'}
        self.top_auth = {'Authorization': f'Basic {secrets["TOP_AUTH"]}'}
        self.nps_gb_auth = {'Authorization': f'Basic {secrets["NPS_GB_AUTH"]}'}
        self.always_data_url = secrets['ALWAYS_DATA_URL']
        self.top_stage_url = secrets['TOP_STAGE_URL']
        self.top_prod_url = secrets['TOP_PROD_URL']
        self.search_mw_url: str = secrets['SEARCH_MW_URL']
        self.search_nps_url: str = secrets['SEARCH_NPS_URL']

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

    def search_mw_by_iew(self, iew: str, body: dict) -> Response:
        url = self.search_mw_url
        body['request']['waybill_number'][0] = iew
        response = requests.post(url, json=body, headers=self.mw_ok)
        return response

    def search_top_by_iew(self, iew: str, body: dict, contour: str = 'ngus'):
        url = self.search_mw_url
        if contour == 'ngus':
            url = url.replace('/npi', '/ngus')
        body['request']['waybill_number'][0] = iew
        response = requests.post(url, json=body, headers=self.top_auth)
        return response

    def search_mw_by_phone(self, phone: str, body: dict) -> Response:
        url = self.search_mw_url
        body['request']['counterparty']['phone_num_main'] = phone
        response = requests.post(url, json=body, headers=self.mw_ok)
        return response

    def search_nps_by_iew(self, iew: str, body: dict) -> Response:
        url = self.search_nps_url
        body['request']['references'][0]['num'] = iew
        response = requests.post(url, json=body, headers=self.nps_gb_auth)
        return response
