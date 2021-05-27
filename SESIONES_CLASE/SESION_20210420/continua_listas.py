# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:49:01 2021

@author: R005
"""
#Adicionar datos por teclado a una lista

varvectornumtec=[]

#Adicionar datos por teclado a la lista
for pos in range (3):
    datoteclado=int(input("Digite valor: "))
    varvectornumtec.append(datoteclado)#Agrega elemento en la ultima posición de la lista
    
print(varvectornumtec)
print()
varvectornumtec.append(4)#Agrega elemento en la ultima posición de la lista    
print("varvectornumtec: ",varvectornumtec)
print()

#Borrar los elementos de la lista
#varvectornumtec.clear()#COn la función .clear si no meto datos en el parentesis borra toda la lista
#print(varvectornumtec)

#Se va a crear otra lista sin pedirla por teclado, o sea que ya tiene datos
varvectornumdos=[2,4,6,8,10]
print("varvectornumdos: ",varvectornumdos)
print()

#Unir dos listas
varvectornumtec.extend(varvectornumdos)#La función .extend permite unir una lista con otra
print("La union de ambas lisas: ",varvectornumtec)
print()

#Conocer los elementos de la lista
tamañovec=len(varvectornumtec)
print("Tamaño de las listas unidas: ",tamañovec)
print()

#Contar las repeticiones de un dato
#si por ejemplo quiero saber cuantas veces repite el 1 en la lista
print("El número deseado se repite: ",varvectornumtec.count(1)," veces")
