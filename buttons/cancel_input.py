from api_requests.logos_requests import Logos
from body.cancel_body import CANCEL_MW_BODY, CANCEL_NPS_BODY
import streamlit as sl
logos = Logos()


def mw_cancel_form():
    with sl.form('Cancel mw by iew'):
        cancel_text = sl.text_input('Cancel by iew')

        submit = sl.form_submit_button('Cancel')
        if all((submit, cancel_text)):
            cancel_result = logos.cancel_waybill_by_iew('mw', cancel_text, CANCEL_MW_BODY)
            sl.write(cancel_result)


def mw_cancel_phone_form():
    pass


def top_cancel_form():
    with sl.form('Cancel top by iew'):
        cancel_text = sl.text_input('Cancel by iew')

        submit = sl.form_submit_button('Cancel')
        if all((submit, cancel_text)):
            cancel_result = logos.cancel_waybill_by_iew('mw', cancel_text, CANCEL_MW_BODY)
            sl.write(cancel_result)


def nps_cancel_form():
    with sl.form('Cancel nps by iew'):
        cancel_text = sl.text_input('Cancel by iew')

        submit = sl.form_submit_button('Cancel')
        if all((submit, cancel_text)):
            cancel_result = logos.cancel_waybill_by_iew('nps', cancel_text, CANCEL_NPS_BODY)
            sl.write(cancel_result)


def nps_cancel_phone_form():
    pass

