# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:39:02 2021

@author: R005
"""
# Lectura de archivos tipo excel 
# Importar librerías
import matplotlib.pyplot as plt
import pandas as pd

#Función de menú
opciones = 0
def menu_datos():
    opci=int(input("Menú de datos\n"+
                  "1.Total goles de equipos de local \n"+
                  "2. Total goles de equipos de visitante \n"+
                  "3. Total goles \n"+
                  "4. goles equipos locales por campeonato \n"+
                  "5. goles equipos visitantes por campeonato \n"+
                  "6. Total goles por campeonato \n"+
                  "7. partidos de local por selección \n"+
                  "8. partidos de local por selección \n"+
                  "9. Fin \n"
                  "Elija una opción : \n"))
    return opci



#Se importa archivo
df_datos=pd.read_excel('Futbol_Partidos.xlsx')
print(df_datos.info())#Muestra una información general de la lista
print(df_datos.head())#para ver como el encabezado
print("\n"*3)#Para dejar renglones vacios


  #1 Goles equipos locales
def gol_local():
    tot_golloc= df_datos['goles_local'].sum()#  Función propia del lenguaje
    return tot_golloc

#2 Goles equipos visitantes
def gol_visitante():
    tot_golvis= df_datos['goles_visita'].sum()#  Función propia del lenguaje
    return tot_golvis

#3 Goles totales
def total_goles():
    tot_gol=gol_local()+gol_visitante()
    return tot_gol
    
#4 goles equipos locales por campeonato
def gol_loc_torneo():
    gloc_ptorneo=df_datos.groupby("torneo").agg({"goles_local":'sum'})
    return gloc_ptorneo

#5 goles equipos visitantes por campeonato
def gol_vis_torneo():
    gvis_ptorneo=df_datos.groupby("torneo").agg({"goles_visita":'sum'})
    return gvis_ptorneo

#6 Goles por campeonato
def tot_gol_torneo():
    gt=df_datos.groupby("torneo").agg({"goles_local":'sum',"goles_visita":'sum'})#Genero df para goles
    golto=gt.loc[:,'goles por torneo']=gt.sum(axis=1)#Calculo total goles
    return golto
    

   
#8partidos local y visitante por selección
def part_loc_sel():
    df_plocal=df_datos.groupby("local").agg({"local":'count'})#Count para contar
    return df_plocal


def part_vis_sel():
    plv_v=df_datos.groupby("visitante").agg({"visitante":'count'})#Count para contar
    return plv_v






print("Goles de los equipos locales: ",gol_local())
print("Goles de los equipos visitantes: ",gol_visitante())
print("Total goles: ",total_goles())
print('\n'*2) #para dejar renglones vacíos
print("Goles de local por torneo: ",gol_loc_torneo())
print('\n'*2) #para dejar renglones vacíos
print("Goles de visita por torneo: ",gol_vis_torneo())
print('\n'*2) #para dejar renglones vacíos
print("Total goles por torneo: ",tot_gol_torneo())
print('\n'*2) #para dejar renglones vacíos




print("Partidos local por selección: ",part_loc_sel())
print()
print("Partidos visitante por selección: ",part_vis_sel())
print('\n'*2) #para dejar renglones vacíos
print('\n'*2) #para dejar renglones vacíos




#graficas



#1 Grafica cantidad de goles equipos locales
fig, ax = plt.subplots()
ax.set_title("GOLES EQUIPOS LOCALES")
ax.set_ylabel("GOLES DE LOCAL")
ax.set_xlabel("EQUIPO")
#crear el gráfico
plt.bar(df_datos['local'],df_datos['goles_local'])
plt.show()

#2 Grafica cantidad de goles equipos visitantes
fig, ax = plt.subplots()
ax.set_title("GOLES EQUIPOS VISITANTES")
ax.set_ylabel("GOLES DE VISITANTE")
ax.set_xlabel("EQUIPO")
#crear el gráfico
plt.bar(df_datos['visitante'],df_datos['goles_visita'])
plt.show()

#3 Grafica cantidad de goles

   

#4 Grafica goles equipos locales por campeonato
fig, ax = plt.subplots()
ax.set_title("GOLES EQUIPOS LOCALES POR CAMPEONATO")
ax.set_ylabel("GOLES DE LOCAL")
ax.set_xlabel("CAMPEONATO")
#crear el gráfico
plt.bar(df_datos['torneo'],df_datos['goles_local'])
plt.show()


#5 Grafica goles equipos visitantes por campeonato
fig, ax = plt.subplots()
ax.set_title("GOLES EQUIPOS VISITANTES POR CAMPEONATO")
ax.set_ylabel("GOLES DE VISITANTE")
ax.set_xlabel("CAMPEONATO")
#crear el gráfico
plt.bar(df_datos['torneo'],df_datos['goles_visita'])
plt.show() 





while opciones != 9:
    opciones = menu_datos()
    
    if opciones ==1:
        gol_local()
        
    if opciones ==2:
        gol_visitante()
        
    if opciones ==3:
        total_goles()
        
    if opciones ==4:
        gol_loc_torneo()
        
    if opciones ==5:
        gol_vis_torneo()
        
    if opciones ==6:
        tot_gol_torneo()
        
    if opciones ==7:
        part_loc_sel()
        
    if opciones ==8:
        part_vis_sel()
    
    if opciones ==9:
        print("Fin del programa")
        
    if opciones > 9:
        print("opcion invalida")