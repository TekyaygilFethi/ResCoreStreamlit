import pandas as pd
from bs4 import BeautifulSoup
import streamlit as st
from helpers import text_helper as th
from collections import defaultdict
from io import BytesIO

def Change(excel_file, en_rescore_file, tr_rescore_file):
    rescore_df = pd.read_excel(excel_file)

    en_res_file_str = en_rescore_file.read().decode("utf-8")
    en_res = BeautifulSoup(en_res_file_str)

    tr_res_file_str = tr_rescore_file.read().decode("utf-8")
    tr_res = BeautifulSoup(tr_res_file_str)

    for index, row in rescore_df.iterrows():
      try:
        en_data = en_res.find('data',  attrs={'name': row['Key']}).find('value')
        en_data.string = row["Value"]

        tr_data = tr_res.find('data',  attrs={'name': row['Key']}).find('value')
        tr_data.string = row["Value (tr-TR)"]

      except Exception as e:
        st.session_state.change_err_log += f"Hata oluştu: {e}\nHata oluşan kayıt:\n{row}\n\n\n"

    st.session_state.change_en_resx_download_data = en_res.prettify().encode('utf-8')
    st.session_state.change_tr_resx_download_data = tr_res.prettify().encode('utf-8')

def Compare(excel_file, en_rescore_file, tr_rescore_file):
    compare_df_dict = defaultdict(list)
    rescore_df = pd.read_excel(excel_file)

    en_res_file_str = en_rescore_file.read().decode("utf-8")
    en_res = BeautifulSoup(en_res_file_str)

    tr_res_file_str = tr_rescore_file.read().decode("utf-8")
    tr_res = BeautifulSoup(tr_res_file_str)

    for index, row in rescore_df.iterrows():
        try:
            is_en_changed = False
            en_data = en_res.find('data',  attrs={'name': row['Key']}).find('value')
            if th.TrimString(en_data.string) != th.TrimString(row["Value"]):
                st.session_state.compare_en_log += f"Yüklenen dosya ile sitede olan yazı farklı!\nKey: {row['Key']}\nSitede gözüken:\n{en_data.string}\nYüklenen:\n{row['Value']}\n\n"
                compare_df_dict["Key"].append(row["Key"])
                compare_df_dict["ExcelEN"].append(row["Value"]) # Olması gereken
                compare_df_dict["WebsiteEN"].append(en_data.string) # Sitede olan
                is_en_changed = True


            tr_data = tr_res.find('data',  attrs={'name': row['Key']}).find('value')
            if th.TrimString(tr_data.string) != th.TrimString(row["Value (tr-TR)"]):
                st.session_state.compare_tr_log += f"Yüklenen dosya ile sitede olan yazı farklı!\nKey: {row['Key']}\nSitede gözüken:\n{tr_data.string}\nYüklenen:\n{row['Value (tr-TR)']}\n\n"
                compare_df_dict["ExcelTR"].append(row["Value (tr-TR)"])  # Olması gereken
                compare_df_dict["WebsiteTR"].append(tr_data.string)  # Sitede olan

                if not is_en_changed:
                    compare_df_dict["ExcelEN"].append("-")  # Olması gereken
                    compare_df_dict["WebsiteEN"].append("-")  # Sitede olan
                    compare_df_dict["Key"].append(row["Key"])

            else:
                if is_en_changed:
                    compare_df_dict["ExcelTR"].append("-")  # Olması gereken
                    compare_df_dict["WebsiteTR"].append("-")

        except Exception as e:
            st.session_state.compare_err_log += f"Hata oluştu: {e}\nHata oluşan kayıt:\n{row}\n\n\n"

    compare_df = pd.DataFrame(compare_df_dict)
    compare_df.rename(columns = {"ExcelEN":"Doğru Değer [EN]", "WebsiteEN":"Sitedeki Yanlış Değer [EN]", "ExcelTR":"Doğru Değer [TR]", "WebsiteTR":"Sitedeki Yanlış Değer [TR]"}, inplace = True)
    st.session_state.compare_download_data = compare_df.to_csv(index=False).encode('utf-8')
