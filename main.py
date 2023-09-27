import streamlit as st
from helpers import streamlit_events as se, streamlit_helper as sh

st.title("ResCore İşlemleri")
st.caption("Excel dosyasından ResCore güncellemek ve Kıyaslamak için bu sayfayı kullanabilirsiniz!")

st.info("UYARI: Hata alırsanız lütfen sayfayı yenileyin!")

tab1, tab2 = st.tabs(["Excel Üzerinden ResCore Kontrol Et", "Excel'den ResCore Güncelle"])

tab1_payload = {}
tab2_payload = {}

sh.SetInitialStreamlitStates()

with tab1:
    file_col1, file_col2, file_col3 = st.columns(3)

    with file_col1:
        tab1_payload["rescore_excel"] = st.file_uploader("ResCore.xlsx dosyasını yükleyin", type=["xlsx"], key ="compare_excel_uploader")
    with file_col2:
        tab1_payload["rescore_en"] = st.file_uploader("ResCore.en-US.resx dosyasını yükleyin", type=["resx"], key ="compare_en_resx_uploader")
    with file_col3:
        tab1_payload["rescore_tr"] = st.file_uploader("ResCore.tr-TR.resx dosyasını yükleyin", type=["resx"], key ="compare_tr_resx_uploader")

    st.text_area(label="Türkçe Dil Kayıtları Log", key="compare_tr_log", value="", height=300)
    st.text_area(label="İngilizce Dil Kayıtları Log", key="compare_en_log", value="", height=300)
    st.text_area(label="Hata Kayıtları Log", key="compare_err_log", value="", height=300)

    footer_col_1, footer_col_2 = st.columns(2)

    with footer_col_1:
        st.button("Gönder", key="compare_submit_button", on_click=se.on_submit_compare_button, args=(tab1_payload,))
    with footer_col_2:
        if st.session_state.compare_download_data is not None:
            st.download_button(
                label="Download CSV File",
                data=st.session_state.compare_download_data,
                file_name="rescore_compare.csv",
                key="compare_download_button"
            )

    if st.session_state.compare_is_success:
        st.success(st.session_state.compare_success_message, icon="✅")
    if st.session_state.compare_is_error:
        st.error(st.session_state.compare_error_message, icon="🚨")

with tab2:
    file_col4, file_col5, file_col6 = st.columns(3)

    with file_col4:
        tab2_payload["rescore_excel"] = st.file_uploader("ResCore.xlsx dosyasını yükleyin", type=["xlsx"], key ="change_excel_uploader")
    with file_col5:
        tab2_payload["rescore_en"] = st.file_uploader("ResCore.en-US.resx dosyasını yükleyin", type=["resx"], key ="change_en_resx_uploader")
    with file_col6:
        tab2_payload["rescore_tr"] = st.file_uploader("ResCore.tr-TR.resx dosyasını yükleyin", type=["resx"], key ="change_tr_resx_uploader")

    change_download_col_1, change_download_col_2, change_download_col_3 = st.columns(3)

    with change_download_col_1:
        st.button("Gönder", key="change_submit_button", on_click=se.on_submit_change_button, args=(tab2_payload,))

    with change_download_col_2:
        if st.session_state.change_en_resx_download_data is not None:
            st.download_button(
                label="EN RESX Dosyasını indir",
                data=st.session_state.change_en_resx_download_data,
                file_name="ResCore.resx",
                key="change_en_resx_download_button"
            )
    with change_download_col_3:
        if st.session_state.change_tr_resx_download_data is not None:
            st.download_button(
                label="TR RESX Dosyasını İndir",
                data=st.session_state.change_tr_resx_download_data,
                file_name="ResCore.tr-TR.resx",
                key="change_tr_resx_download_button"
            )


    if st.session_state.change_is_success:
        st.success(st.session_state.compare_success_message, icon="✅")
    if st.session_state.change_is_error:
        st.error(st.session_state.compare_error_message, icon="🚨")



