# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:34:11 2021

@author: R005

Realizar un programa que permita cargar dos listas de 15 valores cada una.
Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un
algoritmo.

"""

x=1
suma1=0
suma2=0
print("primer lista")
while x<=15:
    valor=int(input("Ingrese valor:"))
    suma1=suma1+valor
    x=x+1
print("Segunda lista: ")
x = 1
while x<=15:
    valor=int(input("Ingrese valor:"))
    suma2=suma2+valor
    x=x+1
if suma1>suma2:
    print("Lista 1 mayor.")
else:
    if suma2>suma1:
        print("Lista2 mayor.")
    else:
        print("Listas iguales.")