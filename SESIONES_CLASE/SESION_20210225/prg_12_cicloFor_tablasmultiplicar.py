# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:37:12 2021

@author: R005
"""

#Leer una tabla de multiplicar e imprimir dicha tabla desde el 1 hasta el 20
#y sumar sus resultados. Usar para la solución ciclo For


#Declarar variables

tabla=0
resultado=0
sumaresultados=0
conrepciclo=1
multiplicador=1

#Leer el número de la tabla para la cual vamos a realizar las operaciones

tabla=int(input("Tabla:"))
#Leer el multiplicador
multiplicador=int(input("multiplicador:"))

#Inicio del ciclo
for conrepciclo in range(multiplicador+1):
    print ("Recorrido tabla va en:", conrepciclo)
    resultado=tabla*conrepciclo
    sumaresultados=sumaresultados+resultado
    print(tabla,"*",conrepciclo, "=",resultado)
#Se impprime la suma por fuera del ciclo
print("La suma de los resultados es :",sumaresultados)
