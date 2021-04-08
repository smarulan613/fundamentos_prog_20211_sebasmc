# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:16:35 2021

@author: R005

Desarrollar un programa que permita la carga de 10 valores por teclado y
nos muestre posteriormente la suma de los valores ingresados y su promedio.
Este problema ya lo desarrollamos, lo resolveremos empleando la estructura
for para repetir la carga de los diez valores por teclado.

"""
suma=0
for f in range(10):
    valor=int(input("Ingrese valor:"))
    suma=suma+valor
print("La suma es")
print(suma)
promedio=suma/10
print("El promedio es:")
print(promedio)
