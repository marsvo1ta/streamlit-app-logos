import requests
from requests import Response
from streamlit import secrets
from analyze_nps_country.analyze_nps_country_by_iew import analyze_country
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
        self.track_url: str = secrets['TRACK_URL']
        self.cancel_url = secrets['CANCEL_URL']
        self.cancel_url_2 = secrets['CANCEL_URL_2']

    def choice_dict(self) -> dict:
        choice = {
            'mw': {
                'auth': self.mw_ok,
                'url': self.cancel_url
            },
            'top': {
                'auth': self.top_auth,
                'url': self.cancel_url
            },
            'nps': {
                'auth': self.nps_gb_auth,
                'url': self.cancel_url_2
            }
        }
        return choice

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

    def get_api_order(self, iew: str, body: dict) -> str:
        response = self.search_nps_by_iew(iew, body).json()
        api_order = [i['num'] for i in response['result'][0]['references'] if i['type'] == 'api_order'][0]
        return api_order

    def search_nps_by_phone(self, phone: str, body: dict) -> Response:
        url = self.search_nps_url
        body['request']['counterparty']['phone_num_main'] = phone
        response = requests.post(url, json=body, headers=self.nps_gb_auth)
        return response

    def get_track(self, project: str, iew: str, body: dict) -> Response:
        url = self.track_url
        choice = {'mw': self.mw_ok, 'top': self.top_auth, 'nps': self.nps_gb_auth}
        try:
            body['request']['references'][0]['num'] = iew
        except KeyError:
            print(body['request'])
        response = requests.post(url, json=body, headers=choice[project])
        return response

    def cancel_waybill_by_iew(self, project: str, iew: str, body: dict) -> Response:
        choice = self.choice_dict()
        url = f"{choice[project]['url']}?waybill_number={iew}" if project != 'nps' else f"{choice[project]['url']}"
        headers = choice[project]['auth'] if project != 'nps' else analyze_country(iew)
        if project == 'nps':
            body['request']['api_order'] = iew
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 404:
            url = url.replace('/npi', '/ngus')
            response = requests.post(url, json=body, headers=choice[project]['auth'])
        return response.json()

    def cancel_waybill_by_phone(self, project: str, phone: str, body: dict) -> Response:
        pass
