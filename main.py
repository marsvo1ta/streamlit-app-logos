import streamlit as sl
from buttons.create_top_buttons import create_top
from buttons.search_input import mw_search_form, top_search_form, mw_search_phone_form, nps_search_form, \
    nps_search_phone_form

create_tab, search_tab = sl.tabs(["Create TOP", "Search"])

with create_tab:
    sl.write("   ")
    ngus_tab, npi_tab = sl.tabs(["Create NGUS", "Create NPI"])
    with ngus_tab:
        create_top('ngus')
    with npi_tab:
        create_top('npi')

with search_tab:
    mw_tab, top_tab, np_sh_tab = sl.tabs(["MW", "TOP", "NPSH"])

    with mw_tab:
        iew_tab, phone_tab = sl.tabs(["IEW", "Phone"])

        with iew_tab:
            mw_search_form()
        with phone_tab:
            mw_search_phone_form()

    with top_tab:
        top_search_form()

    with np_sh_tab:
        iew_tab, phone_tab = sl.tabs(["IEW", "Phone"])

        with iew_tab:
            nps_search_form()
        with phone_tab:
            nps_search_phone_form()

