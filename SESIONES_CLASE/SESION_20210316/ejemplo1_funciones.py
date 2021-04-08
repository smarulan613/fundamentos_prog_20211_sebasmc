# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:06:30 2021

@author: SEBASTIAN MARULANDA CORREA
leer e una venta ek nombre del artíulo vendido, la cantidad del artículo y el valor.
Nos piden calcular:
    *Valor a pagar neto
    *valor del IVA, conociendo que el IVA es el 19%
    *Valor total a pagar

"""
#Factura de venta

def f_titulo():
    print("CALCULO VALOR FACTURA")
    
def f_despedida():
    print("....ADIOS.......")


def f_valorfactura(): #Encabezado de la función
    #Desarrollo de la función

    #Definición de variables
    
    ve_nomArt=""
    ve_canArt=0
    ve_valUniArt=0.0
    
    #Constante
    cons_porIva=0.19
    
    #Variables de proceso y salida
    
    vps_netpag=0.0
    vps_ivapag=0.0
    vps_totpag=0.0
    
    
    #Entrada de datos
    ve_nomArt=input("Artículo: ")
    ve_canArt= int(input("Cantidad: "))
    ve_valUniArt=float(input("Valor Unitario: "))
    
    #Procesos
    vps_netpag=ve_canArt*ve_valUniArt
    vps_ivapag=vps_netpag*cons_porIva
    vps_totpag=vps_netpag+vps_ivapag


    #Salidas
    print("Neto: ",vps_netpag)
    print("IVA: ",vps_ivapag)
    print("Total: ",vps_totpag)

# Llamado a la función

f_titulo()
f_valorfactura()
f_despedida()