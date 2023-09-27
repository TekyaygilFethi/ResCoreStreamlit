import streamlit as st

def SetInitialStreamlitStates():
    if 'compare_is_success' not in st.session_state:
        st.session_state.compare_is_success = False

    if 'compare_is_error' not in st.session_state:
        st.session_state.compare_is_error = False

    if 'change_is_success' not in st.session_state:
        st.session_state.change_is_success = False

    if 'change_is_error' not in st.session_state:
        st.session_state.change_is_error = False

    if 'compare_error_message' not in st.session_state:
        st.session_state.compare_error_message = ""

    if 'compare_success_message' not in st.session_state:
        st.session_state.compare_success_message = ""

    if 'change_error_message' not in st.session_state:
        st.session_state.change_error_message = ""

    if 'change_success_message' not in st.session_state:
        st.session_state.change_success_message = ""

    if 'compare_download_data' not in st.session_state:
        st.session_state.compare_download_data = None

    if 'change_en_resx_download_data' not in st.session_state:
        st.session_state.change_en_resx_download_data = None

    if 'change_tr_resx_download_data' not in st.session_state:
        st.session_state.change_tr_resx_download_data = None


def PopupError(section, error_message):
    if section == "compare":
        st.session_state.compare_is_error = True
        st.session_state.compare_is_success = False
        st.session_state.compare_error_message = error_message
    elif section == "change":
        st.session_state.change_is_error = True
        st.session_state.change_is_success = False
        st.session_state.change_error_message = error_message

def PopupSuccess(section, success_message):
    if section == "compare":
        st.session_state.compare_is_success = True
        st.session_state.compare_is_error = False
        st.session_state.compare_success_message = success_message
    elif section == "change":
        st.session_state.change_is_success = True
        st.session_state.change_is_error = False
        st.session_state.change_success_message = success_message

def ClearLogs(section):
    if section == "compare":
        st.session_state.compare_tr_log = ""
        st.session_state.compare_en_log = ""
        st.session_state.compare_err_log = ""
    elif section == "change":
        st.session_state.change_tr_log = ""
        st.session_state.change_en_log = ""
        st.session_state.change_err_log = ""