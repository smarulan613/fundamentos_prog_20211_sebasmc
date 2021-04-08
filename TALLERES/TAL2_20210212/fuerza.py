# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:26:27 2021

@author: SEBASTIAN MARULANDA CORREA
"""
#Calcular la fuerza que se debe aplicar a un cuerpo para moverlo en
#una mesa horizontal, sabiendo que tiene una masa m (kg) y un
#coeficiente de rozamiento estático  Us.

m=float(input("Suponiendo que el cuerpo está en reposo digite la masa del vuerpo en kilogramos:"))
us=float(input("digite el coeficiente de rozamiento estático:"))
fs=us*m*9.8
print("la fuerza a aplicar al cuerpo en Newton es:",fs)

