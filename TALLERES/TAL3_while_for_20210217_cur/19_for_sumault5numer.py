# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:56:15 2021

@author: R005

Desarrollar un programa que solicite la carga de 10 números e imprima la suma
de los últimos 5 valores ingresados

"""

suma=0
for f in range(10):
    valor=int(input("Ingrese un valor:"))
    if f>4:
        suma=suma+valor
print("La suma de los últimos 5 valores es")
print(suma)
