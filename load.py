import datetime
import re
import streamlit as st

import pandas as pd


def project_ended(end_date: datetime.datetime) -> str:
    end_date = pd.to_datetime(end_date)
    return "Ended" if end_date < datetime.datetime.now() else "Ongoing"


def remove_weird_chars(text: str) -> str:
    text = re.sub(r"¤+", " ", text)
    return text


def load_data(
    file_: st.runtime.uploaded_file_manager.UploadedFile | None,
) -> pd.DataFrame:
    if file_ is not None:
        df = pd.read_csv(file_, sep=";")
    else:
        df = pd.read_csv("./data/export.csv", sep=";")
    df["ProjectAbstractSv"] = df["ProjectAbstractSv"].fillna("")
    df["ProjectAbstractEn"] = df["ProjectAbstractEn"].fillna("")
    df["InvolvedPeople"] = df["InvolvedPeople"].fillna("")
    df["InvolvedPeople"] = df["InvolvedPeople"].apply(remove_weird_chars)
    df["Scbs"] = df["Scbs"].fillna("")
    df["Scbs"] = df["Scbs"].apply(remove_weird_chars)
    df["FundingStartDate"] = pd.to_datetime(df["FundingStartDate"])
    df["FundingEndDate"] = pd.to_datetime(df["FundingEndDate"])
    df["ProjectStatus"] = df["FundingEndDate"].apply(project_ended)
    return df
