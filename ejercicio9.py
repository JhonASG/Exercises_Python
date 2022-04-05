def generar_n_caracteres(n,c):
    i = 0
    mult_c = str()
    while i < int(n):
        mult_c += c
        i += 1
    return mult_c
    
caracter = input("Ingresa el caracter a generar: ")
entero = input("Ingresa la cantidad de veces que deseas ver el caracter: ")

print("El resultado es "+generar_n_caracteres(entero,caracter))