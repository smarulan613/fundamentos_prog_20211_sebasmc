# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:47:17 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#Calcular la velocidad a la que debe ir un vehículo para recorrer una
#distancia d en un tiempo t.

d=float(input("la distancia recorrida en metros es:"))
t=float(input("El tiempo transcurrido al recorrer la distancia en segundos es:"))
v_ms=d/t
v_kh=v_ms*3.6
print("la velocidad promedio en metros/segundo a la que va el vehículo es:",v_ms)
print("la velocidad promedio en kilometros/hora a la que va el vehículo es:",v_kh)