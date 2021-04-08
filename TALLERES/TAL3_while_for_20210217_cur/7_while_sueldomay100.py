# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:27:37 2021

@author: R005
"""

#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado e informe
#cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
#Además el programa deberá informar el importe que gasta la empresa en sueldos
#al personal.

cantidade=int(input("Digite cantidad de empleados: "))#Cantidad empleados
contadore=1 #Contador de cantidad de empleados
salarios_menores=0
salarios_mayores=0
importe=0
while contadore<=cantidade:
    salario=int(input("Digite el salario: "))
    if salario>300:
        salarios_mayores=salarios_mayores+1
    else:
        salarios_menores=salarios_menores+1        
    contadore=contadore+1 #Incrementa la cantidad de empleados
    importe=importe + salario
print()
print("Empleados con salario mayor a 300: ",salarios_mayores)
print()
print("Empleados con salario menor a 300: ",salarios_menores)
print()
print("EL importe de salarios es : $",importe)