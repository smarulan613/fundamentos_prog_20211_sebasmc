# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:26:07 2021

@author: R005

Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
                                                               
b) Cantidad de triángulos de cada tipo.

"""

cant1=0
cant2=0
cant3=0
n=int(input("Ingrese la cantidad de triángulos:"))
for f in range(n):
    lado1=int(input("Ingrese lado 1:"))
    lado2=int(input("Ingrese lado 2:"))
    lado3=int(input("Ingrese lado 3:"))
    if lado1==lado2 and lado1==lado3:
        print("Es un triángulo equilatero.")
        cant1=cant1+1
    else:
        if lado1==lado2 or lado1==lado2 or lado2==lado3:
            print("Es un triángulo isósceles.")
            cant2=cant2+1
        else:
            print("Es un triángulo escaleno.")
            cant3=cant3+1

print("Cantidad de triángulos equilateros: ")
print(cant1)
print("Cantidad de triángulos isósceles: ")
print(cant2)
print("Cantidad de triángulos escalenos: ")
print(cant3)