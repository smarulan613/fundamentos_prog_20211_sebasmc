# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:34:13 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#Realice un programa que resuelva lo siguiente: Si n Empleados  realizan una actividad en k horas,
#¿cuántos empleados se necesitarán para realizar la misma actividad en k1 horas?

ne=int(input("digite el número actual de empleados:"))
k=float(input("digite la cantidad actual de horas:"))
k1=float(input("digite la nueva cantidad de horas de horas:"))
###ce=(ne*k1)/k
ce=ne*(k/k1)
print("Para la misma actividad en k1 horas necesita esta cantidad de empleados:",ce)