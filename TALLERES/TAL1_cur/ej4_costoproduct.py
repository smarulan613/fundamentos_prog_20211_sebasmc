# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:53:11 2021

@author: R005
"""

#Realizar la carga del precio de un producto y la cantidad a llevar.
#Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio 
#del producto)

precio=int(input("ingrese el precio del producto:"))
cantidad=int(input("ingrese la cantidad de productos a llevar:"))
importe=precio*cantidad
print("el importe a pagar es")
print(importe)