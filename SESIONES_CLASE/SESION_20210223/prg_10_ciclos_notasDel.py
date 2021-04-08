# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:36:34 2021

@author: Sebastian Marulanda Correa
"""

#Leer 3 notas de un estudiante las 3 notas de los parcialesy calcular su definitiva sabiendo que es por promedio

#Esrtructuras secunciales

#Entradas
#Pedir el nombre del estudiante y sus 3 notas parciales


#Leer la cantidad de estudiantes de un grupo, para cada estudiante leemos sus 3 notas de los parciales y calcular:
    #1. Definitiva por estudiante
    #2.Nota promedio del grupo
    #3.Cantidad de estudiantes qye aprobaron
    #4. cantidad de estudiantes que reprobaron
#Estructuras repetitivas

canEst=int(input("Cantidad de estudiantes :"))

#Inicializar la variable que controla el ciclo
conRep=0
#Variable real p'ara sumar las definitivas del grupo
sumDefGru=0
#Variable para calcular la nota promedio del grupo
proDefGru=0.0

while (conRep < canEst):
    #Instrucciones a repetir

    nomEst=input("nombre estudiante:")
    notUnoEst=float(input("parcial uno:"))
    notDosEst=float(input("parcial dos:"))
    notTresEst=float(input("parcial tres:"))

    #Cálculos
    NotDefEst = (notUnoEst+notDosEst+notTresEst)/3
    
    #Acumulo las definitivas del grupo
    sumDefGru= sumDefGru + NotDefEst

    #Imprimir los restultados - Salidas

    #función para imprimir y sacar la cantidad de decimales deseada
    print (f"La nota definitiva es : {NotDefEst:.2f}")
    
    #Incrementar la variable que controla el ciclo
    conRep = conRep + 1
    
#Calcular el promedio del grupo
notProDefGru= sumDefGru/canEst

#Imprimir la nota promedio del grupo
print (f"2.La nota promedio del rupo es es : {notProDefGru:.2f}")
    
    
    

