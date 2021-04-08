# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:48:25 2021

@author: R005


Imprimir las treinta primeras potencias de 10, es decir, 10 elevado a 1, 
10 elevado a 2, etc. además sumar las potencias calculadas.

Usando for

"""

base=10
potencia=0
suma=0
for i in range (1,31):
    potencia=base**i
    suma=suma + potencia
    print("10 elevado a la ",i," es:",potencia)
    print("la suma acumulada es:",suma)
    print()
    