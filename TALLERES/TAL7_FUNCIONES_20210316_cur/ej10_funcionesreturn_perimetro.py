# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:33:13 2021

@author: Sebastian Marulanda Correa

Ejercicio 10 curso. funciones Python


Elaborar una función que nos retorne el perímetro de un cuadrado pasando como
parámetros el valor de un lado.

"""

def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro


# bloque principal

lado=int(input("Lado del cuadrado:"))
print("El perimetro es:",retornar_perimetro(lado))