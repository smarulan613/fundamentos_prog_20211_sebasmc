# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:21:50 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#Programa que lee N números enteros y calcula su promedio sale
#con un número menor a cero


#Declarar variables
num = 0 #Variable que almacena los números que digita el usuario
suma = 0 #Variable que almacena la suma de los números positivos
medi = 0.0 #Variable que almacena la media
canele = 0 # Variable que almacena la cantidad de números digitados


num= int (input("Número:")) #Lectura del primer número

while (num>0):
    suma = suma + num
    num = int (input("Número:")) #Lectura de los otros números
    canele = canele + 1
    
#Termina el ciclo

if canele!= 0:
    med = suma/canele #Calcular la media
    print ("la media es:",med) # Imprimir la media
else:
    print ("NO hay número para calcular la media")


