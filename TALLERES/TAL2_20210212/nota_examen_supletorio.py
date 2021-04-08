# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:36:49 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#Realice un programa que obtenga la calificación que debe obtenerse en un
#examen supletorio,si se conoce que el promedio incluido el supletorio para
#aprobar debe ser mínimo de 3.5 . El usuario debe ingresar las calificaciones
#en números enteros del primer y segundo bimestre.


pb=int(input("ingrese el valor entero de la calificación del primer bimestre:"))
sb=int(input("ingrese el valor entero de la calificación del segundo bimestre:"))
#pm es el promedio mínimo para ganar la materia
pm=3.5
#co es la calificación minima a obtener en el supletorio
co=pm*3-pb-sb
print("la calificación mínima a obtener en el examen supletorio es:",co)