import streamlit as sl
from body.create_top_body import *
from api_requests.logos_requests import Logos
import pandas as pd


logos = Logos()


def update_request_body(request_body: dict, new_price: str,
                        new_name: tuple, iew: str,
                        partner_code: str = '12') -> None:
    # Оновлення всіх полів, які містять вартість
    request_body['general_cost_info']['declared_cost'] = new_price
    request_body['payment']['additional_services'][0]['cost'] = new_price
    request_body['payment']['additional_services'][0]['domestic_currency_cost'] = new_price
    request_body['invoices'][0]['invoice_details'][0]['cost_per_unit'] = new_price
    request_body['invoices'][0]['invoice_details'][0]['subtotal_cost_per_good'] = new_price

    # Оновлення інших полів
    request_body['consignee']['name'] = " ".join(new_name)
    request_body['api_order'] = iew
    request_body['references'][0]['num'] = iew
    request_body.update({'partner_code': partner_code})

    return None


def create_top(contour: str):
    body = {'ngus': TOP_NGUS_BODY, 'npi': TOP_NPI_BODY}
    with sl.form(f'Create TOP {contour.upper()} Form'):
        request_body = body[contour]['request']
        price = 100
        f_name, l_name = request_body['consignee']['name'].split()

        # Створення текстових полів і отримання значень від користувача
        new_price = sl.text_input('Ціна', value=price)
        new_f_name = sl.text_input('Імʼя отримувача', value=f_name)
        new_l_name = sl.text_input('Прізвище отримувача', value=l_name)
        new_partner_code = sl.text_input('Код партнера', value='12')

        submit = sl.form_submit_button('Submit')

        if submit:
            # Оновлення значень у словнику
            iew = logos.read_iew(contour).json()
            update_request_body(request_body, new_price, (new_f_name, new_l_name), iew, new_partner_code)
            response = logos.iew_create(contour, request_body)
            if response.status_code == 201:
                data = response.json()
                sl.write(f'Stage: {logos.top_stage_url}/pay?iew={iew}')
                sl.write(f'Prod: {logos.top_prod_url}/pay?iew={iew}')
                df = pd.DataFrame(list(data["result"].items()), columns=["Параметр", "Значення"])
                sl.table(df.set_index("Параметр"))
                logos.write_iew(iew)
            else:
                try:
                    error_message = response.json()['result']['errors'][0]['message']
                    sl.write(f"Error: {error_message}")
                    sl.write(f"IEW: {iew}")
                    if error_message == 'Duplicated reference':
                        logos.write_iew(iew)
                except KeyError:
                    sl.write(response.json())
