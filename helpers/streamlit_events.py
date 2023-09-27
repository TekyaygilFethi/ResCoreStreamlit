from services import rescore_service
from helpers import streamlit_validator as validator, streamlit_helper as sh
import streamlit as st

def on_submit_compare_button(payload):
    sh.ClearLogs("compare")

    excel_file = payload["rescore_excel"]
    en_res = payload["rescore_en"]
    tr_res = payload["rescore_tr"]

    with st.spinner("Dosyalar karşılaştırılırken lütfen bekleyiniz!"):
        if validator.ValidateFiles(excel_file, en_res, tr_res):
            rescore_service.Compare(excel_file, en_res, tr_res)

            sh.PopupSuccess("compare", "Dosya karşılaştırılması tamamlandı!")
        else:
            sh.PopupError("compare", "Dosyalar eksik! Lütfen yüklediğiniz Excel ve ResX dosyalarını kontrol edin!")

def on_submit_change_button(payload):
    sh.ClearLogs("change")

    excel_file = payload["rescore_excel"]
    en_res = payload["rescore_en"]
    tr_res = payload["rescore_tr"]

    with st.spinner("Dosyalar değiştirilirken lütfen bekleyiniz!"):
        if validator.ValidateFiles(excel_file, en_res, tr_res):
            rescore_service.Change(excel_file, en_res, tr_res)

            sh.PopupSuccess("change", "Dosya karşılaştırılması tamamlandı!")
        else:
            sh.PopupError("change", "Dosyalar eksik! Lütfen yüklediğiniz Excel ve ResX dosyalarını kontrol edin!")
