
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:34:55 2021

@author: R005
"""

#  FUNCIÓN DESARROLLADA POR EL PROGRAMADOR
#  ORDENAMIENTO BURBUJA ASCENDENTE
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR - DESCENDENTE")
def ordenamientoBurbujaDescendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]<unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp



unaLista = [2,14,93,17,23,31,15,55,4]
print("Lista Original: ", unaLista)

ordenamientoBurbujaDescendente(unaLista) #llamado a la función
print("Lista ordenada ascendente: ",unaLista)