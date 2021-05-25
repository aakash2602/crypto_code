import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import streamlit as st
import plotly.express as px

st.title("Harvest Vault APYs")
st.markdown('The dashboard will visualize the Harvest.finance vaults APYs from Apr\'21')
st.markdown('')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Vaults accordingly:")

df = pd.read_csv('../harvest_scrapper/harvest_vaults_data.csv', index_col=0)

def remove_pertge(x):
    #print(x)
    x = str(x).replace('%', '').replace('+', '').replace('....','').replace('...', '').strip()
    if '.' in x or '10000' in x:
        return float(x)
    else:
        return 0

df.loc[:, 'vault_apy'] = df['vault_apy'].apply(lambda x: remove_pertge(x))

def remove_time(x):
    return str(x).split(' ')[0]

df = df.reset_index()
df.loc[:, 'index'] = df['index'].apply(lambda x: remove_time(x))
# df = df.set_index('index')

df.columns = ['Date', 'Vault Name', 'Vault Apy', 'Vault Total Assets']

select = st.sidebar.selectbox('Vaults Name', list(df['Vault Name'].drop_duplicates()), key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):

    fig = px.line(df[df['Vault Name']==select], x="Date", y="Vault Apy")
    st.plotly_chart(fig)
    st.title("Vault " + str(select) + " APY plot")

