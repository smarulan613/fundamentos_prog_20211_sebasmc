# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:23:46 2021

@author: R005
"""

import pandas as pd

notafundamentos=pd.DataFrame ({'Nombres':['andres','sebastian','laura','camila'],'semestre':[2,3,3,2]}) #notafundamentos es el dataframe
print(notafundamentos)
print()

notafundamentos.insert(2,'ciudad',['Manizales','Pereira','Manizales','Pereira'])
print(notafundamentos)
print()

notafundamentos['nota1']=4 #Asi también se puede insertar columna haciendo uso del operador
print(notafundamentos)
print()

notafundamentos['nota2']=[3,5,4,4]
print(notafundamentos)
print()

notafundamentos.loc[4]=['maria',2,'Manizales',5,4]
print(notafundamentos)
print()

#Agregar fila con append. se coloca ignore_index ya que los datos no se ingresaron en orden de acuerdo a las columnas entonces asi los ingresa
notafundamentos.append({'semestre':2,'nota1':3,'Nombres':'lucia','ciudad':'Armenia','nota2':5},ignore_index=True)
print(notafundamentos)
print()

#modificar datos iloc. Se indica la posición de lo que quiero que cambie y el dato que deseo que quede
notafundamentos.iloc[2,2]='Pereira'
print(notafundamentos)


