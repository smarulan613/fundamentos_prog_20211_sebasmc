# ==================================================
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR - AMBAS")
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
tipo="descendente"
print("Lista Original: ", unaLista)
ordenamientoBurbuja(unaLista,tipo)
print("Lista Ordenada DE ACUERDO A SU GUSTO: ",unaLista)
    
