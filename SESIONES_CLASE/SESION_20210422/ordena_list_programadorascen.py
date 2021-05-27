# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:30:27 2021

@author: R005
"""

#  FUNCIÓN DESARROLLADA POR EL PROGRAMADOR
#  ORDENAMIENTO BURBUJA ASCENDENTE
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR - ASCENDENTE")
def ordenamientoBurbujaAscendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp



unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original: ", unaLista)

ordenamientoBurbujaAscendente(unaLista) #llamado a la función
print("Lista ordenada ascendente: ",unaLista)