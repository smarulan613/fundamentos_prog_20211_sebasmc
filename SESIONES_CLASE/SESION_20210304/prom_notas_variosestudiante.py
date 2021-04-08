# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:01:35 2021

@author: SEBASTIAN MARULANDA CORREA

Programa que elle el nombre y promedio de notas de 3 amterias (basic,
fortran,pascal) de N estudiantes. Condición de salida nombre=***
"""
#Area de declaración de variables
var_e_nombre="***"
var_e_bas=0.0
var_e_for=0.0
var_e_pas=0.0

var_p_s_conest=0.0
var_p_s_medest=0.0

#Leer nombre
var_e_nom= input("Digite nombre del estudiante: ")

#Ciclo while
while (var_e_nom != "***"):
    var_e_bas= float(input("Digite nota definitiva obtenida en Basic: "))
    var_e_for= float(input("Digite nota definitiva obtenida en Fortran: "))
    var_e_pas= float(input("Digite nota definitiva obtenida en Pascal: "))
    
#Proceso que calcula la media del estudiante
    var_p_s_medest = (var_e_bas+var_e_for+var_e_pas)/3
    print("La media de: ", var_e_nom, "es" ,var_p_s_medest)
    var_e_nom= input("Digite nombre del estudiante: ")
    var_p_s_conest=var_p_s_conest+1
#Fin del ciclo
print("Cantidad de estudiantes: ",var_p_s_conest)
print("Adios...")



