import streamlit as st
import pandas as pd

st.title("Uber Data")
COLUMN_NAME = 'date/time'
URL_ENDPOINT = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(URL_ENDPOINT, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[COLUMN_NAME] = pd.to_datetime(data[COLUMN_NAME])
    return data

data_load_state = st.text('Loading data...')
data = load_data(100)
data_load_state.text("Done! (using st.cache_data)")

st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hour')