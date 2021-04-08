# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:03:58 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#Leer 100 números. Determinar la media de los números positivos y la media de los números negativos

x=1
positivos=0
negativos=0
suma_pos=0
suma_neg=0
media_pos=0
media_neg=0
cantidad=int(input("ingrese la cantidad de números deseada:"))

while x<=cantidad:
    n=int(input("Ingrese número:"))
    
    if n>=0:
        positivos=positivos+1
        suma_pos=suma_pos+n
        media_pos=suma_pos/positivos
    else:
        negativos=negativos+1
        suma_neg=suma_neg+n
        media_neg=suma_neg/negativos
    x=x+1
print("los números ingresados son:",cantidad)
print()
print("La suma de los números positivos es:",suma_pos)
print("La media de los números positivos es:",media_pos)
print("La suma de los números negativos es:",suma_neg)
print("La media de los números negativos es:",media_neg)