# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:24:08 2021

@author: R005
"""

matriz=[[7,8,3],[1,9,2], [4,6,5]]

#suma de todos los elementos de la matriz
sumelemat=0
for f in range (3):
    for c in range (3):
        
        sumelemat=sumelemat+matriz[f][c]
        print("El valor de la posicion [",f,"][",c,"]=",matriz[f][c]) #para ver cada posición (lo puse yo)
        print()
        print("la suma de los elementos es: ",sumelemat) #suma elementos de la lista
        print()
       
       
        
#Para sumar la diagonal principal
sumdiapri=0
for pos in range (3):
    sumdiapri=sumdiapri+matriz[pos][pos]
    print("Posición diagonal: ",matriz[pos][pos]) 
    print()
print("Diagonal principal: ",sumdiapri)
print()

#Imprimiendo la matriz sin corchetes
for f in range (3):
    for c in range (3):
        print(matriz[f][c],end=" ")
    print()




         