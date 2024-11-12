import streamlit as sl
from buttons.create_top_buttons import create_top
from buttons.search_input import mw_search_by_iew_input, top_search_by_iew_input

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
        with sl.form('MW search'):
            sl.write("   ")
            search_text_mw = sl.text_input("Search by iew number")
            sl.write(search_text_mw)
            
            submit = sl.form_submit_button()
            if submit:
                search_result = mw_search_by_iew_input(search_text_mw)
                sl.write(search_result)
    with top_tab:
        with sl.form('TOP search'):
            sl.write("   ")
            search_text_top = sl.text_input("Search by iew number")
            sl.write(search_text_top)

            submit = sl.form_submit_button()
            if submit:
                search_result = top_search_by_iew_input(search_text_top)
                sl.write(search_result)
