# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:41:51 2021

@author: R005
"""

#Métodos de ordenamiento

#Crear lista y darle valores

listabase=[34,12,45,2,60,34,8]
print("Lista base desordenada: ",listabase)

#Ordenar la lista con una función de python de manera ascendente
listabase.sort() #Sin nada en el parentesis de sort ordena ascendente

#Imprimir lista ordenada ascendente
print("Lista base ordenada ascendente: ",listabase)

#Ordenar vista descendente
#Colocando dentro del parentesis de .sort reverse=true ordena descendente
listabase.sort(reverse=True)

#Imprimir lista ordenada descendente
print("Lista base ordenada descendente: ",listabase)