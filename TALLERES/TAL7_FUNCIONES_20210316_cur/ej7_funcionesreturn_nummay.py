# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:16:18 2021

@author: Sebastian Marulanda Correa

Ejercicio 7 curso. funciones Python

Confeccionar una función que le enviemos como parámetros dos enteros y nos
retorne el mayor.

"""
def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor


# bloque principal
valor1=int(input("Ingrese el primer valor:"))
valor2=int(input("Ingrese el segundo valor:"))
print(retornar_mayor(valor1,valor2))
