# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:51:12 2021

@author: SEBASTIAN MARULANDA CORREA
"""
pb=float(input("ingrese el precio base del producto:"))
iv=float(input("ingrese el porcentaje % del iva según el pais:"))
iva=iv/100
pi=pb*iva
pd=pb*0.05
pf=pb+pi-pd
print("el valor a pagar es:",pf)
