# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:45:40 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#Calcular el área de un círculo y longitud de su circunferencia
#importo limreria math para que traiga varios decimales del número pi

import math

radio=float(input("digite el radio de la circunferencia:"))
area_circ=math.pi * pow(radio, 2)
print("El area de la circunfenrecia es:")
print (area_circ)
longitud_circ=2*math.pi*radio
print("La longitud de la circunferencia es:")
print (longitud_circ)