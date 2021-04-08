# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:57:31 2021

@author: SEBASTIAN MARULANDA CORREA

Imprimir las treinta primeras potencias de 10, es decir, 10 elevado a 1, 
10 elevado a 2, etc. además sumar las potencias calculadas.

Usando while

"""
base=10
exponente=0
potencia=0
suma=0
while exponente <30:
    potencia=base**(exponente+1)
    exponente=exponente+1
    suma=suma + potencia
    print("10 elevado a la ",exponente," es:",potencia)
    print("la suma acumulada es:",suma)
    print()
