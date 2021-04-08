# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:49:27 2021

@author: SEBASTIAN MARULANDA CORREA

Escribir un programa que calcule la suma de los cuadrados de los 100 primeros números enteros
con ciclo while

"""
import math
n=1
cuadrado=0
suma=0

while n<=100:    
    cuadrado=math.pow(n, 2)
    suma=suma+cuadrado
    print ("n es:",n)
    print ("cuadrado es:",cuadrado)
    print ("suma es acumulada de los cuadrados de los números es:",suma)
    print()
    n=n+1
    