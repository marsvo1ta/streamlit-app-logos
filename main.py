import streamlit as sl
from buttons.create_top_buttons import create_top
from email_validation.validate_email import authenticate_user, is_valid_email
from cookies_saver.cookies_manager import initialize_cookies, is_authenticated, set_authenticated
from buttons.cancel_input import (
    mw_cancel_form,
    mw_cancel_phone_form,
    top_cancel_form,
    nps_cancel_form,
    nps_cancel_phone_form
)

from buttons.search_input import (
    mw_search_form,
    top_search_form,
    mw_search_phone_form,
    nps_search_form,
    nps_search_phone_form,
)


cookies = initialize_cookies()
if cookies is None:
    sl.stop()


def main():
    if "authenticated" not in sl.session_state:
        sl.session_state.authenticated = is_authenticated(cookies)  # Авто-аутентифікація, якщо вже вхід виконано

    if sl.session_state.authenticated:
        show_application()
    else:
        email = sl.text_input("Введіть ваш email:")

        if sl.button("Увійти") and email:
            if authenticate_user(email):
                sl.session_state.authenticated = True
                set_authenticated(cookies, True)
                sl.rerun()  # 🔹 Оновлення сторінки одразу після аутентифікації
            elif not is_valid_email(email):
                sl.error("Email не валідний")
            else:
                sl.error("Ваш email ще не був доданий в систему")


def show_create_tab():
    sl.write("   ")
    ngus_tab, npi_tab = sl.tabs(["Create NGUS", "Create NPI"])
    with ngus_tab:
        create_top("ngus")
    with npi_tab:
        create_top("npi")


def show_search_tab():
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


def show_cancel_tab():
    mw_tab, top_tab, np_sh_tab = sl.tabs(["MW", "TOP", "NPSH"])

    with mw_tab:
        iew_tab, phone_tab = sl.tabs(["IEW", "Phone"])

        with iew_tab:
            mw_cancel_form()
        with phone_tab:
            mw_cancel_phone_form()

    with top_tab:
        top_cancel_form()

    with np_sh_tab:
        iew_tab, phone_tab = sl.tabs(["IEW", "Phone"])

        with iew_tab:
            nps_cancel_form()
        with phone_tab:
            nps_cancel_phone_form()


def show_application():
    create_tab, search_tab, cancel_tab = sl.tabs(["Create TOP", "Search", "Cancel"])

    with create_tab:
        show_create_tab()

    with search_tab:
        show_search_tab()

    with cancel_tab:
        show_cancel_tab()


if __name__ == "__main__":
    main()
