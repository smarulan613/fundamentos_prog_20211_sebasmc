# Métodos de ordenamiento

# Crear lista y darle valores

listaBase=[34,12,45,2,37,60,34,8]

print("Lista base: ",listaBase)
#Ordenar la lista con una función de python
listaBase.sort()
print("Lista base Ordenada Ascendente: ",listaBase)
  
#Ordenar la lista con una función de python
listaBase.sort(reverse=True)
print("Lista base Ordenada Descendente: ",listaBase)

#==========================================
#  FUNCIÓN DESARROLLADA POR EL PROGRAMADOR
#  ORDENAMIENTO BURBUJA ASCENDENTE
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR - ASCENDENTE")
def ordenamientoBurbujaAscendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

# ============================================
#  FUNCIÓN DESARROLLADA POR EL PROGRAMADOR
#  ORDENAMIENTO BURBUJA DESCENDENTE
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR - DESCENDENTE")
def ordenamientoBurbujaDescendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]<unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [2,14,93,17,23,31,15,55,4]
print("Lista Original: ", unaLista)

ordenamientoBurbujaDescendente(unaLista)
print("Lista Ordenada Descendente: ",unaLista)

# ==================================================

print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR - DESCENDENTE")
def ordenamientoBurbuja(unaLista,tipo):
    if(tipo=="ascendente"):    
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range(numPasada):
                if unaLista[i]>unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp    
                    
                    
    if(tipo=="descendente"):    
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range(numPasada):
                if unaLista[i]<unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp    
        
    
    
    
    
    
#===== FIN DEL DESARROLLO DE LA FUNCIÓN ===================    
unaLista = [2,14,93,17,23,31,15,55,4]
print("Lista Original: ", unaLista)
tipo="ascendente"
ordenamientoBurbuja(unaLista,tipo)
print("Lista Ordenada Descendente: ",unaLista)
    







