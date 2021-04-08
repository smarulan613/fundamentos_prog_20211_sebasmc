# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:50:51 2021

@author: R005
"""

#Escribir un programa que solicite ingresar 10 notas
#de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

altas=0
bajas=0
x=1
while x<=10:
    nota=int(input("ingrese las notas:"))
    if nota>=7:
        altas=altas+1
    else:
        bajas=bajas+1
    x=x+1
print("cantidad de alumnos con notas mayores o iguales que 7:")
print(altas)
print("cantidad de alumnos con notas menores que 7:")
print(bajas)    