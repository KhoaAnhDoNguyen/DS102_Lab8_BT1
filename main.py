import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.title('Data Visualization')

st.header('Upload data file')
data_file = st.file_uploader('Choose a csv file', type=(['.csv']))

if data_file is not None:
  df = pd.read_csv(data_file)
  st.header('Show data')
  st.dataframe(df)

  st.header('Desciptive statistics')
  st.table(df.describe())

  st.header('Show Data Information')
  buffer = io.StringIO()
  df.info(buf = buffer)
  st.text(buffer.getvalue())

   #Visualize each attribute
  st.header('Visualize each attribute')
  for col in list(df.columns):
    fig, ax = plt.subplots()
    ax.hist(df[col], bins = 20)
    plt.xlabel(col)
    plt.ylabel('Quatity')
    st.pyplot(fig)
