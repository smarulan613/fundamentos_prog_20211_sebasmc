# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:31:46 2021

@author: Sebastian Marulanda Correa

2021-04-13

"""

#Practica_1 con arreglos-vectores

#Almacenar en un vector las 5 notas del parcial

#Declarar el vector Lista
listanotas=[]
sumanotas=0.0

#Asignar valores a la lista con un ciclo
for poslista in range (5):
    #Leer desde teclado la nota
    notaest=float(input("Digite nota: ")) #Este es el ingreso de escalares
    sumanotas=sumanotas+notaest
    #Almacenamos la escalar en el arrego (lista)
    #la función .append permite ir agregando los valores en cada posición de la lista
    listanotas.append(notaest) 
    
    
#Imprimir el arreglo
print()
print(listanotas)
print("La suma de las notas es: ",sumanotas)