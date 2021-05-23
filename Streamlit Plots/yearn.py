import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import streamlit as st
import plotly.express as px

st.title("Yearn Vault APYs")
st.markdown('The dashboard will visualize the Yearn vaults APYs from Apr\'21')
st.markdown('')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Vaults accordingly:")

df = pd.read_csv('../yearn_scrapper/yearn_vaults_data.csv', index_col=0)

def remove_pertge(x):
    x = str(x).replace('%', '')
    if '.' in x:
        return float(x)
    else:
        return 0

df.loc[:, 'vault_apy'] = df['vault_apy'].apply(lambda x: remove_pertge(x))

def remove_time(x):
    return str(x).split(' ')[0]

df = df.reset_index()
df.loc[:, 'index'] = df['index'].apply(lambda x: remove_time(x))
# df = df.set_index('index')

# df = df.reset_index()
df.columns = ['Date', 'Vault Name', 'Vault Type', 'Vault Apy', 'Vault Total Assets']
# df.columns

select = st.sidebar.selectbox('V2 Vaults Name', list(df[df['Vault Type']=='v2']['Vault Name'].drop_duplicates()), key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):

    fig = px.line(df[df['Vault Name']==select], x="Date", y="Vault Apy")
    st.plotly_chart(fig)
    st.title("Vault " + str(select) + " APY plot")

select1 = st.sidebar.selectbox('V1 Vaults Name', list(df[df['Vault Type']=='v1']['Vault Name'].drop_duplicates()), key='2')
if not st.sidebar.checkbox("Hide", True, key='2'):
    
    fig = px.line(df[df['Vault Name']==select1], x="Date", y="Vault Apy")
    st.plotly_chart(fig)
    st.title("Vault " + str(select1) + " APY plot")
