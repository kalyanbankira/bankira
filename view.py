import numpy as np
import pandas as pd
import streamlit as st
def app(car_df):
    
    st.header("View Data")
    with st.beta_expander("View dataset"):
        st.table(car_df)

    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())

    beta_col1, beta_col2, beta_col3 = st.beta_columns(3)

      
    with beta_col1:
        if st.checkbox("Show all column names"):
            st.table(list(car_df.columns))

    with beta_col2:
        if st.checkbox("View column data-type"):
            st.table(car_df.dtypes)

    with beta_col3:
        if st.checkbox("View column data"):
            column_data = st.selectbox('Select column', tuple(car_df.columns))
            st.write(car_df[column_data])