# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:13:21 2021

@author: R005
"""

matriz=[]

filas=int(input("Ingrese cantidad de filas de la matriz: "))
columnas=int(input("Ingrese cantidad de columnas de la matriz: "))

for i in range (filas):
    matriz.append([0]*columnas)
    
for f in range (filas):
    for c in range (columnas):
        matriz[f][c]=int(input("Elemento %d,%d :"%(f,c)))

print(matriz)
print()

        
