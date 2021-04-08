# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:11:52 2021

@author: SEBASTIAN MARULANDA CORREA
"""
#Calcular el sueldo total a recibir de un empleado. 
#El usuario deberá ingresar el número de horas trabajadas y el valor por cada hora.
#Considere en los cálculos el descuento de seguridad socialy una bonificación
#del 2% para aquellos cuyo sueldo no supere los 300 dólares.

h=int(input("ingrese las horas trabajadas:"))
v=int(input("ingrese el valor económico en dolares por cada hora:"))
#seguridad social
s=float(input("ingrese el porcentaje de aportes a seguridad social este año:"))
sb=h*v

sp=s/100
sd=sb*sp

if sb<300:
    st=sb+sb*0.02-sd
else:
    st=sb-sd
print("El salario base por horas trabajadas es:",sb)
print ("El descuento por seguridad social es:",sd)
print("El salario total es:",st)



