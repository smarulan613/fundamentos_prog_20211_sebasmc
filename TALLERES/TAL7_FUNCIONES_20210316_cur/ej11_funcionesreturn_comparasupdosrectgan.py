# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:36:57 2021

@author: Sebastian Marulanda Correa

Ejercicio 11 curso. funciones Python


Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
    
def retornar_superficie(lado1,lado2):
    
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cual de los dos tiene una superficie mayor.

"""

def retornar_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie


la1r1=int(input("Digite primer lado del rectangulo 1: "))
la2r1=int(input("Digite segundi lado del rectangulo 1: "))
suprect1=retornar_superficie(la1r1,la2r1)
print("la superficie del primer rectangulo es: ",retornar_superficie(la1r1,la2r1))
print()
    
la1r2=int(input("Digite primer lado del rectangulo 2: "))
la2r2=int(input("Digite segundo lado del rectangulo 2: "))
suprect2=retornar_superficie(la1r2,la2r2)
print("la superficie del primer rectangulo es: ",retornar_superficie(la1r2,la2r2))
print()
if suprect1==suprect2:
    print("Ambos rectangulos tienen la misma superficie")
else:
    if suprect1>suprect2:
        print("la superficie del primer rectangulo es mayor: ",retornar_superficie(la1r1,la2r1))
    else:
        print("la superficie del segundo rectangulo es mayor: ",retornar_superficie(la1r2,la2r2))