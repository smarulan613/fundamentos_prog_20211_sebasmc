# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:58:14 2021

@author: Sebastian Marulanda Correa

Ejercicio 12 curso. funciones Python

Plantear una función que reciba un string en mayúsculas o minúsculas y retorne
la cantidad de letras 'a' o 'A'

"""

def cantidad_vocal_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=='a' or palabra[x]=="A":
            cant=cant+1
    return cant


# bloque principal

palabra=input("Ingrese una palabra:")
print("La palabra",palabra,"tiene",cantidad_vocal_a(palabra),"a")