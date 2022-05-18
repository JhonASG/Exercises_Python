from audioop import mul


def sum(lista):
    suma = 0
    for c in lista:
        suma += c
    return suma
    
def mult(lista):
    multi = 1
    for c in lista:
        multi *= c
    return multi

lista = [41,1,24,4]
print("La suma de la lista "+str(lista)+" es "+str(sum(lista)))
print("La multiplicación de la lista "+str(lista)+" es "+str(mult(lista)))