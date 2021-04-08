# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:38:13 2021

@author: SEBASTIAN MARULANDA CORREA

Escribir un programa que calcule la suma de los cuadrados de los 100 primeros números enteros
Se usa ciclo for

"""

suma=0
for i in range (1,101):
    suma=suma+(i**2)
    print ("El valor de i es: ",i)
    print("El cuadrado de i es: ",i**2)
    print("la suma es acumulanda es :",suma)
    print()