# -*- coding: utf-8 -*-
"""
Created on Thu May 13 18:34:51 2021

@author: R005
"""
#Ejercicio que almacena en listas-procesa en funciones
#Declarar librerias a usar para la solución

import matplotlib.pyplot as plt #plt es un alias para la función matplotlib

#Generar los datos
nombreProducto=['Ron','Aguardiente','Vino','Cerveza','Tequila']
existenciaProducto=[75,50,100,150,40]

#Funciones que resuelven el problema
def f_calc_tot_existencias():
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    
        
    print("Total existencias: ",sumaExistencias)
    
def f_calc_tot_existencias2():#Otra forma usando return
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    return(sumaExistencias)

def f_calc_prom_existencias():
    promExistencias = f_calc_tot_existencias2()/len(existenciaProducto) #se usó len por la cantidad de elementos
    return(promExistencias)
    
    
#Llamado a las funciones que realizan los cálculos
f_calc_tot_existencias()

print("Total Existencias 2: ",f_calc_tot_existencias2())

print("Promedio de Existencias : ",f_calc_prom_existencias())
        
        

#Graficar la información
fig, ax = plt.subplots()
#Definir el título del gráfico
ax.set_title('GRAFICO DE EXISTENCIAS DE PRODUCTOS')
ax.set_xlabel('Productos')
ax.set_ylabel('Existencias')

#Crear el gráfico
plt.bar(nombreProducto,existenciaProducto) #bar hace referencia al tipo de gráfico que es barras

#Publico el gráfico
plt.show()