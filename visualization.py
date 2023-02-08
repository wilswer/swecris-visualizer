import pandas as pd
import plotly.express as px
import streamlit as st

from load import load_data
from st_filter import filter_dataframe


def main() -> None:
    st.title("Swecris Export Tool")
    file_ = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
    if file_ is None:
        st.warning("Please upload a CSV file")
        st.stop()
    df = load_data(file_)
    f_df = filter_dataframe(df)
    st.dataframe(f_df)

    color_col = st.selectbox(
        "Color by",
        ["CoordinatingOrganisationNameSv", "FundingOrganisationNameSv"],
    )
    if st.button("Generate Gantt Chart"):
        fig = px.timeline(
            f_df,
            x_start="FundingStartDate",
            x_end="FundingEndDate",
            y="ProjectTitleSv",
            color=color_col,
        )
        fig.update_yaxes(autorange="reversed")

        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
