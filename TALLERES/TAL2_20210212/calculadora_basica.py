# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:10:41 2021

@author: SEBASTIAN MARULANDA CORREA
"""

#Realice un programa que simule una calculadora básica, con las operaciones:
#suma, resta, multiplicación, división y potencia.

n1=float(input("digite el primer número:"))
n2=float(input("digite el segundo número:"))
s=n1+n2
print ("El resultado de la suma de los número es:",s)

r=n1-n2
print ("El resultado de la resta de los número es:",r)
m=n1*n2
print ("El resultado de la multiplicación de los número es:",m)

if n2!=0:
 d=n1/n2
 
 print ("El resultado de la división de los número es:",d)

p=n1**n2
print ("El resultado elevar el primer número al segundo número es:",p)