import numpy as np
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def app(cars_df):
    st.header("Visualise Data")
    st.set_option("deprecation.showPyplotGlobalUse",False)
    st.subheader("Visualisation Sector")
    ab = st.multiselect("Select the x axis-values:",("carwidth","drivewheel_fwd","horsepower","enginesize"))
    for i in ab:
        st.subheader(f"Scatter plot {i} and prices" )
        plt.figure(figsize=(10,8),dpi = 96)
        sns.scatterplot(x = i,y = 'price',data = cars_df)
        st.pyplot()

    st.subheader("Visualise Selector")
    bc = st.multiselect("Select the charts and plots :",("Histogram","Boxplot","Correlation Heatmap"))
    if "Histogram" in bc:
        st.subheader("Visualise Histogram")
        columns = st.multiselect("select the columns:",('carwidth','horsepower','enginesize'))
        plt.figure(figsize=(10,8),dpi = 96)
        plt.title("Histogram")
        plt.hist(cars_df[columns],bins = 'sturges',edgecolor = 'b')
        st.pyplot()
    
    
    if "Boxplot" in bc:
        st.subheader("Visualise Boxplot")
        columns = st.multiselect("select the values for boxplot:",('carwidth','horsepower','enginesize'))
        plt.title("Boxplot")
        plt.figure(figsize=(10,8),dpi = 96)
        sns.boxplot(cars_df[columns])
        st.pyplot()


    if "Correlation Heatmap" in bc:
        st.subheader("Visualise Correlation Heatmap")
        plt.figure(figsize=(10,8),dpi = 96)
        plt.title("Correlation Heatmap")
        sns.heatmap(cars_df.corr(),annot = True)
        st.pyplot()
        

    
