# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:27:25 2021

@author: Sebastian Marulanda Correa

Ejercicio 9 curso. funciones Python

Elaborar una función que reciba tres enteros y nos retorne el valor promedio
de los mismos

"""

def retornar_promedio(v1,v2,v3):
    promedio=(v1+v2+v3)/3
    return promedio


# bloque principal

valor1=int(input("Ingrese primer valor:"))
valor2=int(input("Ingrese segundo valor:"))
valor3=int(input("Ingrese tercer valor:"))
print("Valor promedio de los tres numeros", retornar_promedio(valor1,valor2,valor3))