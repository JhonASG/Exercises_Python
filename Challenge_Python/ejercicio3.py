def LongitudCadena(cad):
    sum = 0
    for i in cad:
        sum += 1
    return sum

cad = input("Ingresa la lista o la cadena: ")
print("La longitud de la lista o cadena ingresada es "+str(LongitudCadena(cad)))