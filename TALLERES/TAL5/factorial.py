# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:58:33 2021

@author: R005
"""
#Factorial de un número
num=int(input("Digite número del que deea el factorial:"))
factorial=1

for i in range (num):
    factorial=factorial*num
    num=num-1
print ("El factorial es:",factorial)