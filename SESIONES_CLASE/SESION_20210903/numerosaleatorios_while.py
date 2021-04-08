# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:36:56 2021

@author: SEBASTIAN MARULANDA CORREA

Leer N, generar aleatrorios y calcular suma y promedio de:
    números aleatorios, números positivos, números negativos
    
Mostrar los números aleatorios
Mostrar cantidad total de números
Mostrar cantidad de números positivos
Mostrar cantidad de números negativos

Mostrar mayor positivo, menor positivo, mayor negativo, menor negativo

Nota: para saber cuando un número negativo es mayor que otro negativo,
cuanto mas bajo sea el número en valor absoluto (sin signo) mayor será.
"""
#IMportar libreria
import random

#Area de definición de variables

cantidadnumeros=0
contadorrepeticioneshile=0
numero=0
acumuladorsuma=0
promedionumerosaleatotorios=0.0

#Variables segunda parte del ejercicio
acumuladorpositivos=0
acumuladornegativos=0
contadorpositivos=0
contadornegativos=0
promediopositivos=0.0
promedionegativos=0.0

#Variables tercera parte del ejercicio
mayorpositivo=0
mayornegativo=0
menorpositivo=1000 #En este caso el rango es -1000 a 1000 para aleatorios
menornegativo=-1000 #En este caso el rango es -1000 a 1000 para aleatorios

#Entradas

cantidadnumeros=int(input("Cantidad de números: "))

#Procesos
#Ciclo While

while contadorrepeticioneshile<cantidadnumeros:
    numero= random.randint(-1000,1000)
    acumuladorsuma=acumuladorsuma+numero
    #Segunda parte del ejercicio
    if numero>0:#Cálculo para números positivos
        print("Número positivo: ",numero)
        acumuladorpositivos=acumuladorpositivos+numero
        contadorpositivos=contadorpositivos+1
        #Tercera parte del ejercicio
        #Identificar el mayor de los positivos
        if numero>mayorpositivo:
            mayorpositivo=numero
        
        #Identificar el menor de los positivos
        if numero<menorpositivo:
            menorpositivo=numero
    else:#Cálculos para números negativos
        print("Número negativo: ",numero)
        acumuladornegativos=acumuladornegativos+numero
        contadornegativos=contadornegativos+1
        
        #Identificar el mayor de los negativos
        if numero<mayornegativo:
            mayornegativo=numero
        
        #Identificar el menor de los negativos
        if numero>menornegativo:
            menornegativo=numero
        
    #Fin de la segunda parte del ejercicio
       
    contadorrepeticioneshile=contadorrepeticioneshile+1
    
#FIn ciclo
#Cálculo de promedios

promedionumerosaleatotorios=acumuladorsuma/contadorrepeticioneshile
promediopositivos=acumuladorpositivos/contadorpositivos
promedionegativos=acumuladornegativos/contadornegativos

#Salidas de todos los números
print("Suma de numeros aleatorios:",acumuladorsuma)
print("Promedio de numeros aleatorios:",promedionumerosaleatotorios)

#Salidas de todos los números positivos
print("Cantidad números positivos: ",contadorpositivos)
print("suma de numeros positivos: ",acumuladorpositivos)
print("Promedio de numeros positivos: ",promediopositivos)

#Salidas de todos los números negativos
print("Cantidad números negativos: ",contadornegativos)
print("suma de numeros negativos: ",acumuladornegativos)
print("Promedio de numeros negativos: ",promedionegativos)

#Imprimir mayor de los positivos y menor de los positivos
print("Mayor de los positivos: ",mayorpositivo)
print("Menor de los positivos: ",menorpositivo)

#Imprimir mayor de los negativos y menor de los negativos
print("Mayor de los negativos: ",menornegativo)
print("Menor de los negativos: ",mayornegativo)