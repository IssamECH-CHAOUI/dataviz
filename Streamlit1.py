#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import numpy as np

#readind masi data
dfmasi = pd.read_csv("Masi.csv")

dfmasi.columns = ['Séance', "Masi", 'variation']

#Masi
num = []
for i in np.array(dfmasi[["Masi"]]):
    num.append(float(i[0].replace(",",".")))
dfmasi[["Masi"]] = pd.DataFrame(num)

dfmasi = dfmasi.sort_values(by="Séance")
#Variation
num1 = []
for i in np.array(dfmasi[["variation"]]):
    num1.append(float(i[0].replace(",",".")))
dfmasi[["variation"]] = pd.DataFrame(num1)


#make seance as index and convert it to datetime
dfmasi = dfmasi.set_index('Séance')
dfmasi.index = pd.to_datetime(dfmasi.index, format = "%d/%m/%Y")

dfmasi.head()

dfmasi = dfmasi.sort_values(by="Séance")
Rm = [-100+100*dfmasi[["Masi"]].iloc[i][0]/dfmasi[["Masi"]].iloc[i-1][0] for i in range(1,len(dfmasi))]
Rm = [np.nan] +Rm

dfmasi["Rentabilité m"] = Rm

dfmasi = dfmasi.iloc[59:]


header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()


with header:
    st.title("Issam ECH-CHAOUI")

    
with dataset:
    st.header("Masi dataset")
    st.line_chart(dfmasi[["Masi"]])






