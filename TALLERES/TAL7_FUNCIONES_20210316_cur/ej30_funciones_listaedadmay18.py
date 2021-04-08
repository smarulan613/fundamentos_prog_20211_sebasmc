# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:16:18 2021

@author: Sebastian Marulanda Correa

Ejercicio 30 curso. funciones Python

Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)

"""
def cantidad_mayores18(edad1,*edades):
    cant=0
    if edad1>=18:
        cant=cant+1
    for x in range(len(edades)):
        if edades[x]>=18:
            cant=cant+1
    return cant


# bloque principal

print("La cantidad de personas mayores a 18 son:", cantidad_mayores18(1,9,5,30,50))