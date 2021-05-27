# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:31:46 2021

@author: Sebastian Marulanda Correa

2021-04-19

"""

#Practica_1 con arreglos-vectores

#Almacenar en un vector las 5 notas del parcial

#Declarar el vector Lista
listanotas=[]
sumanotas=0.0
nganadas=0.0
nperdidas=0.0

#Asignar valores a la lista con un ciclo
for poslista in range (5):
    #Leer desde teclado la nota
    notaest=float(input("Digite nota: ")) #Este es el ingreso de escalares
    sumanotas=sumanotas+notaest
    #Almacenamos la escalar en el arrego (lista)
    #la función .append permite ir agregando los valores en cada posición de la lista
    listanotas.append(notaest)
    if notaest>=3:
        nganadas=nganadas+1
    else:
        nperdidas=nperdidas+1
    
promedio=sumanotas/5    
#Imprimir el arreglo
print()
print(listanotas)
print("La suma de las notas es: ",sumanotas)
print("El promedio de las notas es: ",promedio)
print()
print("La cantidad de notas ganadas es: ",nganadas)
print("La cantidad de notas perdidas es: ",nperdidas)
