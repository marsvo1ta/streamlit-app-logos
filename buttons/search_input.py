import streamlit as sl
from api_requests.logos_requests import Logos
from body.search_body import SEARCH_MW_BODY, SEARCH_MW_BODY_PHONE, SEARCH_NPS_BODY, SEARCH_NPS_BODY_PHONE
from body.track_body import TRACK_BODY

logos = Logos()


def mw_search_by_iew_input(iew: str) -> dict:
    response = logos.search_mw_by_iew(iew, SEARCH_MW_BODY)
    return response.json()


def top_search_by_iew_input(iew: str) -> dict:
    response = logos.search_top_by_iew(iew, SEARCH_MW_BODY)
    return response.json()


def mw_search_by_phone_input(phone: str) -> dict:
    response = logos.search_mw_by_phone(phone, SEARCH_MW_BODY_PHONE)
    return response.json()


def nps_search_by_iew_input(iew: str) -> dict:
    response = logos.search_nps_by_iew(iew, SEARCH_NPS_BODY)
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

        submit = sl.form_submit_button()
        if all((submit, search_text_mw)):
            search_result = mw_search_by_iew_input(search_text_mw)
            sl.write(search_result)


def top_search_form():
    with sl.form('TOP search'):
        search_text_top = sl.text_input("Search by iew number")
        submit = sl.form_submit_button()
        if all((submit, search_text_top)):
            search_result = top_search_by_iew_input(search_text_top)
            sl.write(search_result)


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
        search_text_nps = sl.text_input("Search by iew number")
        submit = sl.form_submit_button('Search')
        if all((submit, search_text_nps)):
            search_result = nps_search_by_iew_input(search_text_nps)
            sl.write(search_result)


def nps_search_phone_form():
    with sl.form('NPS search by phone'):
        sl.write("   ")
        search_text_nps = sl.text_input("Search by phone number")
        search_submit = sl.form_submit_button('Search')
        if all((search_submit, search_text_nps)):
            search_result = nps_search_by_phone_input(search_text_nps)
            sl.write(search_result)



def nps_track_form():
    with sl.form('NPS track'):
        search_text_nps = sl.text_input("Get track by iew number")
        submit = sl.form_submit_button('Get track')
        if all((submit, search_text_nps)):
            search_result = get_track_input('nps', search_text_nps)
            if search_result:
                tracking_history = search_result['result']['data'][0]['tracking_history']
                short_track_info = []
                for track in tracking_history:
                    short_track_info.append({track['code']: track['description']})
            sl.json(short_track_info)


