# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:44:26 2021

@author: SEBASTIAN MARULANDA CORREA
"""
#solicita al usuario ingresar por teclado 3 números diferentes
print("ingrese 3 numeros enteros diferenetes")
#Variable denominada e tipo entero, para solicitar al usuario que ingrese 1 o 2 según el orden
#en que desea que se organicen los números
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor"))
#Variable denominada a, tipo entero, para solicitar al usuario que ingrese por teclado el primer número
a = int(input("ingrese el numero a"))
#Variable denominada b, tipo entero, para solicitar al usuario que ingrese por teclado el segundo número
b = int(input("ingrese el numero b"))
#Variable denominada c, tipo entero, para solicitar al usuario que ingrese por teclado el tercer número
c = int(input("ingrese el numero c"))
#Utiliza condicional if para que al usar el operador == compare e con 1 y si es verdadero ejecute a la línea siguiente
#basicamente desde este condicional si el usuario escogió la opción 1 al principio del programa ejecutaría algortimo
#oganizando los números de mayor a menor
if (e == 1):  
#Una vez el usuario ha seleccionado la opción 1, se empieza a comparar a como el mayor respecto a b y c    
#si se cumple la condición anterior se compara si a es mayor que b  
    if (a > b):
#si se cumple la condición anterior se compara si a es mayor que c          
        if (a > c):
#si se cumple la condición anterior se compara si b es mayor que c              
            if(b > c):
#si se cumplen las condiciones anteriores se imprima el resultado de las variables en orden a,b,c  siendo a el mayor,
#b el valor medio y c el menor               
               print(a, b, c)
#si no se cumplen las condiciones anteriores             
            else:
#se imprime los número en orden a,c,b. Siendo a el mayor, c el intermedio y b el menor
               print(a, c, b)
#Una vez el usuario ha seleccionado la opción 1, se empieza a comparar c como el mayor respecto a a y b                
#Si c es mayor que a ejecuta línea siguiente               
    if (c > a):
#si c es mayor que b ejecuta la siguiente línea        
        if (c > b):
#si b es mayor que a ejecuta la siguiente línea             
            if(b > a):
#al cumplir las ultimas condiciones anteriores imprime los números en orden c,b,a. siendo c el mayor, b el intermedio
#y a el menor                
               print(c, b, a)
#si no se cumple lo anterior               
            else:
#imprime c como el mayor, a el intermedio y b el menor                
               print(c, a, b)
#Una vez el usuario ha seleccionado la opción 1, se empieza a comparar b como el mayor respecto a a y c
#Si b es mayor que a se ejecuta la siguiente línea                
    if (b > a):
#Si b es mayor que c se ejecuta la siguiente línea         
        if (b > c):
#Si a es mayor que c se ejecuta la siguiente línea             
            if(a > c):
#al cumplir las ultimas condiciones anteriores imprime los números en orden b,a,c. siendo b el mayor, a el intermedio
#y c el menor                 
               print(b, a, c)
#si no se cumplen estas condiciones entonces               
            else:
#imprime b como el mayor, c el intermedio y a el menor                
               print(b, c, a)

#Utiliza condicional if para que al usar el operador == compare e con 2 y si es verdadero ejecute a la línea siguiente
#basicamente desde este condicional si el usuario escogió la opción 2 al principio del programa ejecutaría algortimo
#oganizando los números de menor a mayor
if (e == 2):
#Una vez el usuario ha seleccionado la opción 2, se empieza a comparar a como el menor respecto a b y c    
#si se cumple la condición anterior se compara si a es menor que b    
    if (a < b):
#si a es menor que c ejecuta la siguiente línea        
        if (a < c):
#si b es menor que c ejecuta siguiente línea            
            if(b < c):
#dado el cumplimiento de condiciones anteriores se imprimirian los números en orden a,b c, siendo a el menor,
#b el intermedio y c el mayor                
               print(a, b, c)
# si no se cumplen condiciones anteriores               
            else:
# se imprime a como el menor, c el intermedio y b el mayor                
               print(a, c, b)
#se empieza a comparar si c es menor respecto a a y b
#compara si c es menor que a              
    if (c < a):
#compara si c es menor que b        
        if (c < b):
#compara si b es menor que a            
            if(b < a):
#al cumplir las ultimas condiciones imprime los números en oren c, b, a siendo c el menor, b intermedio y a mayor                
               print(c, b, a)
#si no se cumplen               
            else:
#se imprime en orden c,a b siendo c el menor, a el intermedio y b el mayor                
               print(c, a, b)
#por ultimo se compara si b es el menor respecto a a y c
#inicialmente compara si b es menor que a               
    if (b < a):
#luego si b es menor que c        
        if (b < c):
#si a es menor que c            
            if(a < c):
#si se cumplen las condiciones se imprime en orden b,a,c siendo b el menor, a el intermedio y c el mayor                
               print(b, a, c)
#de lo contrario               
            else:
#se imprime b como el menor, c el intermedio y a el mayor
               print(b, c, a)
#dado el caso que si de los 3 números ingresados, dos o mas son iguales se ejecutarían las siguienes líneas.
#dependiendo los que se detecten como iguales entre si, se le mostrarian al usuario
#se compara si a es igual a b
if (a == b):
#si es verdadera la sentencia anterior entonces se imprime al usuario la indicación que b y a son iguales    
    print("b y a son iguales")
#se compara si a es igual respecto a c    
    if (a == c):
#si lo anterior fuese cierto se imprimiría que a y c son iguales        
        print("a y c son iguales")
#se compara si b es igual respecto a c        
        if(b == c):
#si lo anterior es cierto se imprime que b y c son iguales            
           print(" b y c con iguales")
#Por ultimo se comparan los tres números           
           if(a == b == c):
#si se determina que todos son iguales se imprime esta sentencia al usuario               
              print("todos son iguales")