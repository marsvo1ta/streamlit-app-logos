import streamlit as sl
from buttons.create_top_buttons import create_top

tab1, tab2 = sl.tabs(["Create NGUS", "Create NPI"])
with tab1:
    create_top('ngus')
with tab2:
    create_top('npi')