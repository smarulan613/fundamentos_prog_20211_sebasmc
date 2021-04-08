# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:04:21 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#leer las notas de una clase de informática y deducir todas aquellas que son notables (>=7 y <9)

x=1
notables=0
cantidad=int(input("ingrese la cantidad de notas:"))
while x<=cantidad:
    nota=float(input("las notas son:"))
    if nota >=7:
        if nota<9:
            notables=notables +1
    x=x+1
print("la cantidad de calificaciones notables es:",notables)