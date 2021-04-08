# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:08:15 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#Realice un programa que obtenga el índice de masa corporal de una persona,
#ingresando la estatura en centímetros y el peso en kilos.

estatura_cm=int(input("digite su estatura en centrimetros:"))
estatura_m=estatura_cm/100
peso=int(input("digite su peso en kilogramos:"))
imc=peso/pow(estatura_m,2)
print("su indice de masa corporal es:",imc)
