# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 17:34:16 2025

@author: Maria G
"""

import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

# Mostrar o cargar los datos
#ds = pd.read_csv("dataset_financiero_riesgo.csv")

# Colocar un titulo principal en la página Web
st.title("Predicción de Riesgo Financiero")

# Cargar los datos en la memoria CACHE para mejorar la velocidad del acceso al 
# conjunto de datos
@st.cache_data 

# Hacemos una funcion que se llama cargar_datos. Leemos el archivo en una variable
# y retornamos la variable al que llama a la función. En este caso la variable 
# que retornamos se llama "ds", abreviatura de "dataset".
def cargar_datos():
    ds = pd.read_csv("dataset_financiero_riesgo.csv")
    return ds

ds = cargar_datos()
st.write("Vista previa de los datos")
st.dataframe(ds.head())

# preprocesamiento de datoso del conjunto de datos

ds_encode = ds.copy()#Copia el dataset completo a otro dataset

label_cols = ["Historial_Credito", "Nivel_Educacion"]
le = LabelEncoder()
for col in label_cols:
    ds_encode[col] = le.fit_transform(ds_encode[col])
    
x = ds_encode.drop("Riesgo_Financiero", axis=1) #elimina la variavle dependiente
y = ds_encode["Riesgo_Financiero"]
y = LabelEncoder().fit_transform(y)    

# Dividir el conjunto de datos en entrenamiento y testng
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Entrenamiento del modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=0 )
modelo.fit(x_train, y_train)
score = modelo.score(x_test,y_test) 

st.subheader(f"Precision del modelo: {score:.2f}") 

# MAtriz de confusion, nos sirve para validar que datos nos sirven y que otros datos no nos sirven
y_pred = modelo.predict(x_test)
mc= confusion_matrix(y_test, y_pred)
st.subheader("Matrix de Confución")
fig, ax = plt.subplots()


sns.heatmap(mc, annot=True, fmt="d", cmap="Blues", ax = ax )
st.pyplot(fig)











    













