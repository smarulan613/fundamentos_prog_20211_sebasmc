# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:33:04 2021

@author: R005

Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene
un promedio de edades mayor.

"""
em=5
sumamañana=0

et=6
sumatarde=0

en=11
sumanoche=0

for x in range (em):
    edadm=int(input("Digite edades estudiantes de la mañana:"))
    sumamañana=sumamañana+edadm
    promediomañana=sumamañana/em
print ("Promedio edades estudiantes de la mañana: ",promediomañana)
print()


for x in range (et):
    edadt=int(input("Digite edades estudiantes de la tarde:"))
    sumatarde=sumatarde+edadt
    promediotarde=sumatarde/et
print ("Promedio edades estudiantes de la tarde: ",promediotarde)
print()

for x in range (en):
    edadn=int(input("Digite edades estudiantes de la noche:"))
    sumanoche=sumanoche+edadn
    promedionoche=sumanoche/en
print ("Promedio edades estudiantes de la noche: ",promedionoche)
print()

if promediomañana>promediotarde and promediomañana>promedionoche:
    print ("La jornada con mayor promedio de edad es mañana")
else:
    if promediotarde>promediomañana and promediotarde>promedionoche:
        print ("La jornada con mayor promedio de edad es tarde")
    else:
        print ("La jornada con mayor promedio de edad es noche")