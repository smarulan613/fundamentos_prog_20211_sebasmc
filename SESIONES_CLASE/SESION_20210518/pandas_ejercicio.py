# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:49:20 2021

@author: R005
"""

import pandas as pd

#Leer archivo de excel. La idea es que el archivo a cargar esté en la misma carpeta que el .py
df_archivoExcel = pd.read_excel('ventas_productos_1.xlsx',index_col="Producto")
df_archivoExcel = df_archivoExcel[:10].copy()#Para definir cuantas o que filas quiero 
print(df_archivoExcel)
print('\n'*2) #para dejar renglones vacíos

#Grafica vertical
df_archivoExcel.plot(kind='bar') #La grafica en la consola se ve en plots

#Grafica horizontal
df_archivoExcel.plot(kind='barh') #La grafica en la consola se ve en plots

df_archivoExcel.plot(kind='barh',width=1) #con width se define el ancho(separación entre barras)