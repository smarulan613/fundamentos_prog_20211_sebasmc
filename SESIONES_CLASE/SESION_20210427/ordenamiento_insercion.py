# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:11:01 2021

@author: R005
"""

def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual

unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoPorInsercion(unaLista)
print(unaLista)