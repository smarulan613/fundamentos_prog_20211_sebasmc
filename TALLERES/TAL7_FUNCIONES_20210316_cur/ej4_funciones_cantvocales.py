# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 09:46:05 2021

@author: R005

Desarrollar una funcion que reciba un string como parametro y
nos muestre la cantidad de vocales. Llamarla desde el bloque
principal del programa 3 veces con string distintos.


Observaciones:
Tener en cuenta que en el if todas están en minuscula    
    
En cadena al usar .lower() Al imprimir Las mayusculas las pasa a minusculas.

En cadena al usar .upper() Al imprimir pasa de minusculas a mayusculas.

En cadena al usar .swapcase Al imprimir pasa de minusculas a mayusculas y mayusculas a
minusculas.

"""

def cantidad_vocales(cadena):
    cadena=cadena.upper() #ver observaciones en encabeado del programa
    print(cadena)
    cant=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u" or cadena[x]=="A" or cadena[x]=="E" or cadena[x]=="I" or cadena[x]=="O" or cadena[x]=="U":
            cant=cant+1
    print("Cantidad de vocales de la palabra",cadena,"es",cant)


# bloque principal
cantidad_vocales("hola")
cantidad_vocales("Perro")
cantidad_vocales("CORRERIA")