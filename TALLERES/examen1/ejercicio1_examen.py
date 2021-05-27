# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:40:48 2021

@author: R005


l101202114137 es el el nombre de la variable correspondiente al lado

calcular area y perimetro del triangulo

area=√3/4∗"l101202114137"^2



"""

import math

def mostrar_area(l101202114137): #función para hallar el area
    area=(math.sqrt(3)/4)*(l101202114137**2)# Formula para hallar el area
    return area #retorno a la función

def mostrar_perimetro(l101202114137):#función para hallar el perimetro
    perimetro=l101202114137*3 #Formula del perimetro
    return perimetro #retorno a la unción perimetro
    


l101202114137=float(input("Ingrese el valor del lado: ")) #solicitar al usuario ingresar el lado del triangulo
print ("El area del triangulo es: " ) #se imprime enunciado de area
print(mostrar_area(l101202114137)) #imprime resultado del area
print() #imprimir un espacio entre el area y el perimetro
print ("El perimetro del triangulo es: " ) #se imprime enunciado del perimetro
print(mostrar_perimetro(l101202114137))#se imprime resulatdo del perimetro


    