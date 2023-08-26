from s3_files import download_s3_object
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import boto3
import warnings

warnings.filterwarnings('ignore')
st.set_page_config(page_title="Ventas AdventureWorks",page_icon=":bar_chart:",layout="wide")
st.title(" :bar_chart: DashBoard AdventureWorks ")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>",unsafe_allow_html=True)

# Descarga el .csv de la tabla de hechos de AWS
'''
bucket = 'adventuretransformado'
object = 'FACT-AdventureWorks_part00000.csv'
save_as = 'FACT-AdventureWorks.csv'
download_s3_object(bucket, object, save_as)
'''

# Lectura de csv
df = pd.read_csv("./FACT-AdventureWorks.csv",on_bad_lines='skip',encoding="ISO-8859-1")
df2 = df.copy()
df3 = df.copy()
df4 = df.copy()
df5 = df.copy()
df6 = df.copy()


st.sidebar.header("Choose your filter: ")


territorio = st.sidebar.multiselect("Selecciona el territorio", df["TerritoryName"].unique())
st.subheader("VENTAS POR TERRITORIO")
col1,col2,col3,col4=st.columns((4))
filtered_df = df[df["TerritoryName"].isin(territorio)]
with col1:
    category_df = filtered_df.groupby(by=["Anio"], as_index=False)["TotalDue"].sum()
    fig = px.bar(category_df, x="Anio", y="TotalDue", title="POR AÑO",text=['{:.0f}'.format(x) for x in category_df["TotalDue"]],
                 template="seaborn")
    st.plotly_chart(fig, use_container_width=True, height=200)
    fig.update_traces(text=filtered_df["TerritoryName"], textposition="outside")
with col2:
    fig = px.pie(filtered_df, values="TotalDue", names="TerritoryName", title="POR AÑO",hole=0.5)
    fig.update_traces(text=filtered_df["TerritoryName"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

with col3:
    category_df = filtered_df.groupby(by=["Month"], as_index=False)["TotalDue"].sum()
    fig = px.bar(category_df, x="Month", y="TotalDue", text=['{:}'.format(x) for x in category_df["TotalDue"]],
                 template="seaborn",title="POR MES")
    st.plotly_chart(fig, use_container_width=True, height=200)
    fig.update_traces(text=filtered_df["TerritoryName"], textposition="outside")

with col4:
    fig = px.pie(filtered_df, values="TotalDue", names="TerritoryName", hole=0.5,title="POR MES")
    fig.update_traces(text=filtered_df["TerritoryName"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)




country = st.sidebar.multiselect("Selecciona el país",df["Country"].unique())
st.subheader("VENTAS POR PAIS")
col1,col2,col3,col4=st.columns((4))
filtered_df3 = df3[df3["Country"].isin(country)]
with col1:
    category_df3 = filtered_df3.groupby(by=["Anio"], as_index=False)["TotalDue"].sum()
    fig3 = px.bar(category_df3, x="Anio", y="TotalDue", text=['{:.0f}'.format(x) for x in category_df3["TotalDue"]],
                 template="seaborn",title="POR AÑO")
    st.plotly_chart(fig3, use_container_width=True, height=200)
    fig3.update_traces(text=filtered_df3["Country"], textposition="outside")
with col2:
    fig3 = px.pie(filtered_df3, values="TotalDue", names="Country", hole=0.5,title="POR AÑO")
    fig3.update_traces(text=filtered_df3["Country"], textposition="outside")
    st.plotly_chart(fig3, use_container_width=True)
with col3:
    category_df3 = filtered_df3.groupby(by=["Month"], as_index=False)["TotalDue"].sum()
    fig3 = px.bar(category_df3, x="Month", y="TotalDue", text=['{:}'.format(x) for x in category_df3["TotalDue"]],
                 template="seaborn",title="POR MES")
    st.plotly_chart(fig3, use_container_width=True, height=200)
    fig3.update_traces(text=filtered_df3["Country"], textposition="outside")
with col4:
    fig3 = px.pie(filtered_df3, values="TotalDue", names="Country", hole=0.5,title="POR MES")
    fig3.update_traces(text=filtered_df3["Country"], textposition="outside")
    st.plotly_chart(fig3, use_container_width=True)









Continent = st.sidebar.multiselect("Selecciona el continente", df2["Continent"].unique())
st.subheader("VENTAS POR CONTINENTE")
col1,col2,col3,col4=st.columns((4))
filtered_df2 = df2[df2["Continent"].isin(Continent)]
with col1:
    category_df2 = filtered_df2.groupby(by=["Anio"], as_index=False)["TotalDue"].sum()
    fig2 = px.bar(category_df2, x="Anio", y="TotalDue", text=['{:0f}'.format(x) for x in category_df2["TotalDue"]],
                 template="seaborn",title="POR AÑO")
    st.plotly_chart(fig2, use_container_width=True, height=200)
    fig2.update_traces(text=filtered_df2["Continent"], textposition="outside")
with col2:
    fig2 = px.pie(filtered_df2, values="TotalDue", names="Continent", hole=0.5,title="POR AÑO")
    fig2.update_traces(text=filtered_df2["Continent"], textposition="outside")
    st.plotly_chart(fig2, use_container_width=True)
with col3:
    category_df2 = filtered_df2.groupby(by=["Month"], as_index=False)["TotalDue"].sum()
    fig2 = px.bar(category_df2, x="Month", y="TotalDue", text=['{:}'.format(x) for x in category_df2["TotalDue"]],
                 template="seaborn",title="POR MES")
    st.plotly_chart(fig2, use_container_width=True, height=200)
    fig2.update_traces(text=filtered_df2["Continent"], textposition="outside")
with col4:
    fig2 = px.pie(filtered_df2, values="TotalDue", names="Continent", hole=0.5,title="POR MES")
    fig2.update_traces(text=filtered_df2["Continent"], textposition="outside")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("VENTAS POR GENERO")
col1,col2=st.columns((2))
Genero = st.sidebar.multiselect("Selecciona el genero", df4["Gender2"].unique())
filtered_df4 = df4[df4["Gender2"].isin(Genero)]

with col1:
    category_df4 = filtered_df4.groupby(by=["Anio"], as_index=False)["TotalDue"].sum()
    fig4 = px.bar(category_df4, x="Anio", y="TotalDue", text=['${:0f}'.format(x) for x in category_df4["TotalDue"]],
                 template="seaborn",title="POR AÑO")
    st.plotly_chart(fig4, use_container_width=True, height=200)
    fig4.update_traces(text=filtered_df4["Gender2"], textposition="outside")
with col2:
    category_df4 = filtered_df4.groupby(by=["Month"], as_index=False)["TotalDue"].sum()
    fig4 = px.bar(category_df4, x="Month", y="TotalDue", text=['{:}'.format(x) for x in category_df4["TotalDue"]],
                  template="seaborn",title="POR MES")
    st.plotly_chart(fig4, use_container_width=True, height=200)
    fig4.update_traces(text=filtered_df4["Gender2"], textposition="outside")

st.subheader("EMAIL MARKETING")
col1,col2=st.columns((2))
Suscripciones = st.sidebar.multiselect("EmailMarketing", df4["EmailPromotion"].unique())
filtered_df5 = df4[df4["EmailPromotion"].isin(Suscripciones)]

with col1:
    category_df5 = filtered_df5.groupby(by=["Anio"], as_index=False)["TotalDue"].sum()
    fig5 = px.bar(category_df5, x="Anio", y="TotalDue", text=['{:}'.format(x) for x in category_df5["TotalDue"]],
                 template="seaborn",title="POR AÑO")
    st.plotly_chart(fig5, use_container_width=True, height=200)
    fig5.update_traces(text=filtered_df5["EmailPromotion"], textposition="outside")

with col2:
    category_df5 = filtered_df5.groupby(by=["Month"], as_index=False)["TotalDue"].sum()
    fig5 = px.bar(category_df5, x="Month", y="TotalDue", text=['{:}'.format(x) for x in category_df5["TotalDue"]],
                  template="seaborn",title="POR MES")
    st.plotly_chart(fig5, use_container_width=True, height=200)
    fig5.update_traces(text=filtered_df5["EmailPromotion"], textposition="outside")


st.subheader("VENTA DE PRODUCTOS")
col1,col2=st.columns((2))
productos = st.sidebar.multiselect("Nombre del Producto", df4["ProductName"].unique())
filtered_df6 = df6[df6["ProductName"].isin(productos)]

with col1:
    category_df6 = filtered_df6.groupby(by=["Anio"], as_index=False)["TotalDue"].sum()
    fig6 = px.bar(category_df6, x="Anio", y="TotalDue", text=['{:}'.format(x) for x in category_df6["TotalDue"]],
                 template="seaborn",title="POR AÑO")
    st.plotly_chart(fig6, use_container_width=True, height=200)
    fig6.update_traces(text=filtered_df6["ProductName"], textposition="outside")

with col2:
    category_df6 = filtered_df6.groupby(by=["Month"], as_index=False)["TotalDue"].sum()
    fig6 = px.bar(category_df6, x="Month", y="TotalDue", text=['{:}'.format(x) for x in category_df6["TotalDue"]],
                  template="seaborn",title="POR MES")
    st.plotly_chart(fig6, use_container_width=True, height=200)
    fig6.update_traces(text=filtered_df5["ProductName"], textposition="outside")














