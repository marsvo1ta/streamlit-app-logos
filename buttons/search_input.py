import streamlit as sl
from api_requests.logos_requests import Logos
from body.search_body import SEARCH_MW_BODY, SEARCH_MW_BODY_PHONE, SEARCH_NPS_BODY, SEARCH_NPS_BODY_PHONE
from body.track_body import TRACK_BODY

logos = Logos()


def nps_short_search_response(search_result: dict):
    shipper = search_result[0]['shipper']
    consignee = search_result[0]['consignee']
    pickup_address = shipper['pickup_address']
    delivery_address = consignee['delivery_address']
    references = search_result[0]['references']

    fields_to_delete_references = ['partner_alias', 'enable_tracking', 'id', 'data']
    fields_to_delete_address = ['warehouse_data', 'country_data', 'latitude', 'longitude']
    fields_to_delete_entity = ['address', 'service_data']

    for ref in references:
        for field in fields_to_delete_references:
            ref.pop(field, None)

    for field in fields_to_delete_address:
        pickup_address.pop(field, None)
        delivery_address.pop(field, None)

    for field in fields_to_delete_entity:
        shipper.pop(field, None)
        consignee.pop(field, None)


def mw_search_by_iew_input(iew: str) -> dict:
    response = logos.search_mw_by_iew(iew, SEARCH_MW_BODY)
    return response.json()


def top_search_by_iew_input(iew: str) -> dict:
    response = logos.search_top_by_iew(iew, SEARCH_MW_BODY)
    return response.json()


def mw_search_by_phone_input(phone: str) -> dict:
    response = logos.search_mw_by_phone(phone, SEARCH_MW_BODY_PHONE)
    return response.json()


def nps_search_by_iew_input(iew: str, env: str) -> dict:
    response = logos.search_nps_by_iew(iew, SEARCH_NPS_BODY, env)
    return response.json()


def nps_search_by_phone_input(phone: str) -> dict:
    response = logos.search_nps_by_phone(phone, SEARCH_NPS_BODY_PHONE)
    return response.json()


def get_track_input(proj: str, iew: str) -> dict:
    response = logos.get_track(proj, iew, TRACK_BODY)
    return response.json()


def mw_search_form():
    with sl.form('MW search'):
        search_text_mw = sl.text_input("Search by iew number")
        col1, col2 = sl.columns(2)
        with col1:
            search_submit = sl.form_submit_button('Search', use_container_width=True)
        with col2:
            track_submit = sl.form_submit_button('Track', use_container_width=True)
        if all((search_submit, search_text_mw)):
            search_result = mw_search_by_iew_input(search_text_mw)
            sl.write(search_result)
        if all((track_submit, search_text_mw)):
            track_result = get_track_input('mw', search_text_mw)
            print(track_result)
            if track_result:
                tracking_history = track_result['result']['data'][0]['tracking_history']
                short_track_info = []
                for track in tracking_history:
                    short_track_info.append({track['code']: track['description']})
                sl.json(short_track_info)


def top_search_form():
    with sl.form('TOP search'):
        search_text_top = sl.text_input("Search by iew number")
        col1, col2 = sl.columns(2)
        with col1:
            search_submit = sl.form_submit_button('Search', use_container_width=True)
        with col2:
            track_submit = sl.form_submit_button('Track', use_container_width=True)
        if all((search_submit, search_text_top)):
            search_result = top_search_by_iew_input(search_text_top)
            sl.write(search_result)
        if all((track_submit, search_text_top)):
            track_result = get_track_input('top', search_text_top)
            print(track_result)
            if track_result:
                tracking_history = track_result['result']['data'][0]['tracking_history']
                short_track_info = []
                for track in tracking_history:
                    short_track_info.append({track['code']: track['description']})
                sl.json(short_track_info)


def mw_search_phone_form():
    with sl.form('MW search by phone'):
        sl.write("   ")
        search_text_mw = sl.text_input("Search by phone number")

        submit = sl.form_submit_button()
        if all((submit, search_text_mw)):
            search_result = mw_search_by_phone_input(search_text_mw)
            sl.write(search_result)


def nps_search_form():
    with sl.form('NPS search'):
        env_select = sl.selectbox('ENV', ('Prod', 'Stage'))
        search_text_nps = sl.text_input("Search by iew number")
        col1, col2 = sl.columns(2)
        with col1:
            search_submit = sl.form_submit_button('Search', use_container_width=True)
        with col2:
            track_submit = sl.form_submit_button('Track', use_container_width=True)
        if all((search_submit, search_text_nps)):
            search_result = nps_search_by_iew_input(search_text_nps, env_select)
            if search_result.get('result'):
                search_result = search_result['result']
                nps_short_search_response(search_result)
            sl.json(search_result)
        if all((track_submit, search_text_nps)):
            track_result = get_track_input('nps', search_text_nps)
            if track_result:
                tracking_history = track_result['result']['data'][0]['tracking_history']
                short_track_info = []
                for track in tracking_history:
                    short_track_info.append({track['code']: track['description']})
                sl.json(short_track_info)


def nps_search_phone_form():
    with sl.form('NPS search by phone'):
        sl.write("   ")
        search_text_nps = sl.text_input("Search by phone number")
        search_submit = sl.form_submit_button('Search')
        if all((search_submit, search_text_nps)):
            search_result = nps_search_by_phone_input(search_text_nps)
            sl.write(search_result)



