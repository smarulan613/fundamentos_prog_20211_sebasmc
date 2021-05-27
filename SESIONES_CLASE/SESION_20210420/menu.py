# import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	#os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Almacenar las notas en la lista")
	print ("\t2 - Sumar las notas")
	print ("\t3 - tercera opción")
    print ("\t4 - cuara opción")
    
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("1.  inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("1.  ALMACENA LAS NOTAS EN LA LISTA")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("2.  SUMAR LAS NOTAS")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("3.  Calcular el Promedio ")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")