# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:30:45 2021

@author: R005

Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.

"""

num=int(input("Digite cantidad de números:"))
positivos=0
negativos=0
cero=0
multiplos15=0
parespositivos=0
paresnegativos=0
sumapares=0
for x in range (num):
    n=int(input("Digite números: "))
    if n>0:
        positivos=positivos+1
    else:
        if n<0:
            negativos=negativos+1
        else:
            cero=cero +1
    if n%15==0 and n>=15:
        multiplos15=multiplos15+1
    if n%2==0 and n>=2:
        parespositivos=parespositivos+n
    if n%-2==0 and n<=-2:
        paresnegativos=paresnegativos+n
    sumapares=parespositivos+paresnegativos 
    
print()
print("Cantidad positivos: ",positivos)
print("Cantidad negativos: ",negativos)
print("Cantidad cero: ",cero)
print("Cantidad multiplos de 15: ",multiplos15)
print("Acumulado pares: ",sumapares)