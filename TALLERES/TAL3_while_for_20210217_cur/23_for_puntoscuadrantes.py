# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:28:16 2021

@author: R005

Escribir un programa que pida ingresar coordenadas (x,y) que representan
puntos en el plano. Informar cuántos puntos se han ingresado en el primer,
segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se
ingrese la cantidad de puntos a procesar.

"""

cant1=0
cant2=0
cant3=0
cant4=0
n=int(input("Cantidad de puntos:"))
for f in range(n):
    x=int(input("Ingrese coordenada x:"))
    y=int(input("Ingrese coordenada y:"))
    if x>0 and y>0:
        cant1=cant1+1
    else:
        if x<0 and y>0:
            cant2=cant2+1
        else:
            if x<0 and y<0:
                cant3=cant3+1
            else:
                if x>0 and y<0:
                    cant4=cant4+1

print("Cantidad de puntos en el primer cuadrante: ")
print(cant1)
print("Cantidad de puntos en el segundo cuadrante: ")
print(cant2)
print("Cantidad de puntos en el tercer cuadrante: ")
print(cant3)
print("Cantidad de puntos en el cuarto cuadrante: ")
print(cant4)