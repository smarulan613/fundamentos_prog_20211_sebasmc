# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:51:48 2021

@author: R005
"""

#Leer una tabla de multiplicar e imprimir dicha tabla desde el 1 hasta el 20
#y sumar sus resultados. Usar para la solución ciclo While

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

#Inicio del ciclo repetitio
while(conrepciclo <= multiplicador):
    resultado=tabla*conrepciclo
    sumaresultados=sumaresultados+resultado
    print(tabla,"*",conrepciclo, "=",resultado)
    #Incrementar la variable que controla el ciclo
    conrepciclo=conrepciclo+1
print("La suma de los resultados es :",sumaresultados)
    



