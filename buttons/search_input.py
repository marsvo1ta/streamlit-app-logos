import streamlit as sl
from api_requests.logos_requests import Logos
from body.search_body import SEARCH_MW_BODY

logos = Logos()


def mw_input(iew: str):
    response = logos.search_mw_by_iew(iew, SEARCH_MW_BODY)
    return response.json()

