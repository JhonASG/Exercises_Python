def inversaString(c):
    longC = len(c)
    n_c = str()
    for i in range(1, longC+1):
        n_c += c[longC-i]
    return n_c

cad = input("Ingresa la cadena: ")
print(inversaString(cad))