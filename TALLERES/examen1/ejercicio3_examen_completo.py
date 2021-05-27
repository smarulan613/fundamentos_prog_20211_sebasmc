# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 07:50:44 2021
@author: SEBASTIAN MARULANDA CORREA

Punto 3: Se desea obtener la nómina semanal —salario neto— de los N
(Leídos por teclado) empleados   de una empresa, cuyo trabajo se paga por 
horas y del modo siguiente:

• las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa determinada que se debe introducir por teclado al igual que el número de horas
trabajadas, el nombre del trabajador, género  y 1,2 o 3 de acuerdo a la sección donde trabaje
• las horas superiores a 35 se pagarán como extras a un promedio de 1,5 horas normales,
• los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
  Salud 12,5% del salario
  ICBF 4% del salario
  Retención en la fuente según la tabla anexa:
       de 2’000.000 a 3´000.000 5%  de 3’000.001 a 4’000.000 7%  de 4’000.001 a 5’000.000 9%  de 5’000.000 en adelante 11%
Imprima el desprendible de pago detallado para cada empleado
Imprima la planilla de totales de pago de la empresa (Total Empleados, Total Horas, Total extras, pago horas, pago extras, etc)
Imprimir la planilla de totales los acumulados por sección.
Imprimir la planilla de totales los acumulados por género.

"""

cantidad=int(input("Digite cantidad de empleados (as): ")) #SOLICITAR INGRESO DE CANTIDAD DE EMPLEADOS
salud=0.125 #constante porcentual para el descuento de salud
icbf=0.04 #constante porcentual para el descuento de icbf

hextra=1.5 #Constante promedio de incremento por horas extras

totalhorashasta35=0 #acumulador a usar para el total de horas cuando el ciclo se ejecuta dentro de cantidad horas menor o igual a 35
totalhorasmay35=0 #acumulador a usar para el total de horas cuando el ciclo se ejecuta dentro de cantidad horas mayor 35

totalextras=0 #acumulador para la cantidad de horas extras
pagoextras=0 #acumulador para el total de pago de horas extras

pagohoras=0 #acumulador para el pago total de horas


seccion1=0 #acumulador para almacenar el acumulado por sección 1
seccion2=0 #acumulador para almacenar el acumulado por sección 2
seccion3=0 #acumulador para almacenar el acumulado por sección 3

masculino=0 #acumulador para almacenar el acumulado por genero masculino
femenino=0 #acumulador para almacenar el acumulado por genero masculino


for x in range (cantidad): #Definición del ciclo for para que lo ejecute según el número de empleados previamente ingresado
    nt=input("Digite nombre del(a) trabajador (a): " ) #Solicitar digitar nombre del trabajador
    h=int(input("Ingrese cantidad de horas trabajadas: ")) #Solicitar cantidad de horas trabajadas
    hb=int(input("Digite costo base por hora trabajada: "))#variable para el costo de cada hora
    g=int(input("Digite genero del(a) trabajador (a): 1:masculino, 2 femenino: ")) #Solicitar digitar el genero. 
    s=int(input("Digite la sección a la que pertenece el(la) trabajador(a): 1, 2, 3: ")) #solicitar digitar la sección a la que pertenece
    

    
    if h<=35:#condicional para ejecución del ciclo si las horas trabajadas son mejores o iguales a 35 (horas normales sin extras)
        
        totalhorashasta35=totalhorashasta35+h #Se va incrementando el acumulador con horas cuando se ejecuta el ciclo
        sind=hb*h #definición de formula para el salario sin descuentos, cuando el trabajador laboró 35 o menos horas
        pagohoras=pagohoras+sind #Acumulador pago horas trabajadas
        descsalud=sind*salud#Formula para el descuento de salud
        descicbf=sind*icbf#Formula para el descuento del icbf
        
        #condicionales para determinar retefuente de acuerdo a rangos solicitados
        if sind>=2000000 and sind<=3000000:
            rf=sind*0.05
        else:
            if sind>3000000 and sind<=4000000:
                rf=sind*0.07
            else:
                if sind>4000000 and sind<=5000000:
                    rf=sind*0.09
                else:
                    if sind>5000000:
                        rf=sind*0.11
                    else:
                        rf=sind*0
            
        
        cond=sind-(descsalud)-(descicbf)-(rf) #formula para obtener el salario con descuentos cuando se trabajó 35 horas o menos
        print()#imrpimir espacio para facilitar visualización en resultados finales
        print("Nombre empleado(a): ",nt)#Se imprime nombre del empleado
        print("genero: ",g)#Se imprime genero del trabajador
        print("sección: ",s)#Se imprime sección a la que pertenece el trabajador
        print("Horas trabajadas: ",h)#Se imprimen horas laboradas por trabajador
        print("Costo por hora: ",hb)#Se imprime el costo por hora trabajada
        print("salario sin descuentos: ",sind)#Se imprime salario sin descuentos
        print("Descuento salud: ",descsalud)#Se imprime el valor del descuento por concepto de salud
        print("Descuento icbf: ",descicbf)#Se imprime el valor del descuento por concepto de icbf
        print("retefuente: ",rf)#Se imprime el valor del descuento por concepto de retefuente
        print("salario con descuentos: ",cond)#Se imprime el total del salario tras descuentos
    else:#A partir de acá se ejecuta ciclo cuando las horas trabajadas son mayores que 35
        
        totalhorasmay35=totalhorasmay35+h#Se va incrementando el acumulador con horas cuando se ejecuta el ciclo
        canthorasextras=h-35 #para determinar cantidad de horas extras trabajadas o sea por encima de 35
        totalextras=totalextras+canthorasextras#incremento acumulador para el total de horas extras
        incrementoporhoraex=hb*hextra
        coshex=canthorasextras*incrementoporhoraex #costo de cada hora extra por el porcentaje
        pagoextras=pagoextras+coshex#Incremento acumulador pago horas extras
        sind=(35*hb)+coshex #se multiplica costo base de cada hora por cantidad horas y se le suman costo horas extras
        pagohoras=pagohoras+sind #Acumulador pago hora
        
        descsalud=sind*salud#Formula para el descuento de salud
        descicbf=sind*icbf#Formula para el descuento icbf
        
         #condicionales para determinar retefuente sin horas extras de acuerdo a rangos solicitados
        if sind>=2000000 and sind<=3000000:
            rf=sind*0.05
        else:
            if sind>3000000 and sind<=4000000:
                rf=sind*0.07
            else:
                if sind>4000000 and sind<=5000000:
                    rf=sind*0.09
                else:
                    if sind>5000000:
                        rf=sind*0.11
                    else:
                        rf=sind*0
            
        
        cond=sind-(descsalud)-(descicbf)-(rf)#formula para obtener el salario con descuentos cuando se trabajó mas de 35 horas
        
        print()#imrpimir espacio para facilitar visualización en resultados finales
        print("Nombre empleado (a): ",nt)#Se imprime nombre empleado
        print("genero: ",g)#se imprime genero del empleado
        print("sección: ",s)#Se imprime sección a la que pertenece empleado
        print("Horas trabajadas: ",h)#Se imprime cantidad de horas trabajadas
        print("Costo por hora (hasta 35 horas trabajadas): ",hb)#Se imprime costo por hora hasta maximo 35 horas trabajadas
        print("horas extras trabajadas: ",canthorasextras)#Se imprime cantidad horas extras por trabajador
        print("costo unitario cada hora extra: ",incrementoporhoraex)#imprime costo por hora extra
        print("costo total horas extras: ",coshex)#se imprime costo total de horas extras por trabajador
        print("Salario sin descuentos: ",sind)#Imprime salario sin decuentos
        print("Descuento salud: ",descsalud)#imprime decuento de salud
        print("Descuento icbf: ",descicbf)#Imprime descuento icbf
        print("retefuente: ",rf)#Imprime decuento por retefuente dado el caso que aplique
        print("salario con descuentos: ",cond)#Imprime salario cond escuentos
        print()#imrpimir espacio para facilitar visualización en resultados finales
    
        #condicionales para que dependiendo la sección asignada al trabajador almacene lo acumulado
    if s==1:
        seccion1=seccion1+sind #si la sección del trabajador es la 1 va acumulando en su respectiva variable
    else:
        if s==2:
            seccion2=seccion2+sind #si la sección del trabajador es la 2 va acumulando en su respectiva variable
        else:
            if s==3:
                seccion3=seccion3+sind #si la sección del trabajador es la 3 va acumulñando en su respectiva variable
                
         #condicionales para que dependiendodel genero asignado al trabajador almacene lo acumulado       
    if g==1:
        masculino=masculino+sind #incremento para acumulador del genero masculino
    else:
        femenino=femenino+sind #Incremento para acumulador del genero femenino
    
        

totalhoras=totalhorashasta35+totalhorasmay35 #Formula para el total horas indistinto si fueron iguales, menores o mayores que 35

print()#imrpimir espacio para facilitar visualización en resultados finales
print("*****TOTAL PAGOS EMPRESA********")#Para mostrar un titulo de total de pagos emrpesa
print()#imrpimir espacio para facilitar visualización en resultados finales
print("Cantidad de empleados: ",cantidad)   #imprime cantidad total de empleados
print("cantidad horas trabajadas: ",totalhoras)#Imprime total horas trabajadas
print("Total pago horas: ",pagohoras) #Imprime total pago por horas trabajadas
print("Total horas extras: ",totalextras)#Imprime el total de horas extras trabajadas
print("Total pago por horas extras: ",pagoextras)#Imprime el total pagado por concepto de horas extras
print()#imrpimir espacio para facilitar visualización en resultados finales
print("*****ACUMULADOS POR SECCION********")#Para mostrar un titulo de total acumulado por sección
print()#imrpimir espacio para facilitar visualización en resultados finales
print("Cantidad trabajadres (as) sección 1: ",seccion1)#Imprime acumulado por sección 1
print("Cantidad trabajadres (as) sección 2: ",seccion2)#Imprime acumulado pro sección 2
print("Cantidad trabajadres (as) sección 3: ",seccion3)#Imprime acumulado por sección 3
print()#imrpimir espacio para facilitar visualización en resultados finales
print("*****ACUMULADOS POR GENERO********")#Para mostrar un titulo de total acumulados por genero
print()#imrpimir espacio para facilitar visualización en resultados finales
print("Acumulado genero masculino: ",masculino)#Imprime acumulado por genero masculino
print("Acumulado genero femenino: ",femenino)#Imprime acumulado por genero femenino






        


        
        
        
        
        
        
        
        
      
          
            
        
        
        
        
        
        
        
        
        
                 
                 
        


        
        
