import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import boto3
from s3_files import download_s3_object
# Guarda el .csv de la tabla de hechos


warnings.filterwarnings('ignore')
st.set_page_config(page_title="Ventas AdventureWorks",page_icon=":bar_chart:",layout="wide")
st.title(" :bar_chart: DashBoard AdventureWorks ")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>",unsafe_allow_html=True)

'''
bucket = 'adventuretransformado'
object = 'FACT-AdventureWorks_part00000.csv'
save_as = 'FACT-AdventureWorks.csv'

download_s3_object(bucket, object, save_as)


'''


df=pd.read_csv("./FACT-AdventureWorks.csv",on_bad_lines='skip',encoding="ISO-8859-1")
df2=df.copy()
df3=df.copy()
df4=df.copy()

st.sidebar.header("Choose your filter: ")

territorio = st.sidebar.multiselect("Selecciona el territorio", df["TerritoryName"].unique())
st.subheader("Ventas totales realizadas por año por territorio")
col1,col2=st.columns((2))
filtered_df = df[df["TerritoryName"].isin(territorio)]
with col1:
    category_df = filtered_df.groupby(by=["Anio"], as_index=False)["TotalDue"].sum()
    fig = px.bar(category_df, x="Anio", y="TotalDue", text=['${:,.0f}'.format(x) for x in category_df["Anio"]],
                 template="seaborn")
    st.plotly_chart(fig, use_container_width=True, height=200)
    fig.update_traces(text=filtered_df["TerritoryName"], textposition="outside")
with col2:
    fig = px.pie(filtered_df, values="TotalDue", names="TerritoryName", hole=0.5)
    fig.update_traces(text=filtered_df["TerritoryName"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)




country = st.sidebar.multiselect("Selecciona el país",df["Country"].unique())
st.subheader("Ventas totales realizadas por año por país")
col1,col2=st.columns((2))
filtered_df3 = df3[df3["Country"].isin(country)]
with col1:
    category_df3 = filtered_df3.groupby(by=["Anio"], as_index=False)["TotalDue"].sum()
    fig3 = px.bar(category_df3, x="Anio", y="TotalDue", text=['${:,.0f}'.format(x) for x in category_df3["Anio"]],
                 template="seaborn")
    st.plotly_chart(fig3, use_container_width=True, height=200)
    fig3.update_traces(text=filtered_df3["Country"], textposition="outside")
with col2:
    fig3 = px.pie(filtered_df3, values="TotalDue", names="Country", hole=0.5)
    fig3.update_traces(text=filtered_df3["Country"], textposition="outside")
    st.plotly_chart(fig3, use_container_width=True)









Continent = st.sidebar.multiselect("Selecciona el continente", df2["Continent"].unique())
st.subheader("Ventas totales realizadas por año por continente")
col1,col2=st.columns((2))
filtered_df2 = df2[df2["Continent"].isin(Continent)]
with col1:
    category_df2 = filtered_df2.groupby(by=["Anio","Gender"], as_index=False)["TotalDue"].sum()
    fig2 = px.bar(category_df2, x="Anio", y="TotalDue", text=['${:,.0f}'.format(x) for x in category_df2["Anio"]],
                 template="seaborn")
    st.plotly_chart(fig2, use_container_width=True, height=200)
    fig2.update_traces(text=filtered_df2["Continent"], textposition="outside")
with col2:
    fig2 = px.pie(filtered_df2, values="TotalDue", names="Continent", hole=0.5)
    fig2.update_traces(text=filtered_df2["Continent"], textposition="outside")
    st.plotly_chart(fig2, use_container_width=True)


Genero = st.sidebar.multiselect("Selecciona el genero", df2["Gender"].unique())







