# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:09:05 2021

@author: Sebastian Marulanda Correa

Ejercicio 8 curso. funciones Python

Confeccionar una función que le enviemos como parámetro un string y
nos retorne la cantidad de caracteres que tiene. En el bloque
principal solicitar la carga de dos nombres por teclado y llamar a
la función dos veces. Imprimir en el bloque principal cual de las dos
palabras tiene más caracteres.

"""

def mas_caracteres(cadena):
    return len(cadena)

nombre1=input("Digite primer nombre: ")
nombre2=input("Digite segundo nombre: ")  
largo1=mas_caracteres(nombre1)
largo2=mas_caracteres(nombre2)  

if largo1==largo2:
    print("Los nombres ",nombre1," y ",nombre2,"tienen igual cantidad de caracteres: ",largo1)
else:
    if largo1>largo2:
        print("El nombre ",nombre1," tiene mas caraceres: ",largo1)
    else:
        print("El nombre ",nombre2," tiene mas caraceres ",largo2)