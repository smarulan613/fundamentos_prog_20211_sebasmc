# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:20:28 2021

@author: Sebastian Marulanda Correa

Ejercicio 24 curso. funciones Python

Confeccionar una función que reciba un string como parámetro y en forma
opcional un segundo string con un caracter. La función debe mostrar el
string subrayado con el caracter que indica el segundo parámetro


"""
def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


# bloque principal

titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Ventas","-")
