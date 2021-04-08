# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:41:26 2021

@author: Sebastian Marulanda Correa

Ejercicio 27 curso. funciones Python

Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento
separados por una coma.

"""

def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")


# bloque principal

lista=cargar()
imprimir(lista)