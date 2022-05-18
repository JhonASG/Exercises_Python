def palindromo(p):
    LongP = len(p)
    n_p = str()
    for i in range(1, LongP+1):
        n_p += p[LongP-i]
    if p == n_p:
        return True
    else:
        return False

palabra = input("Ingresa la palabra: ")
print("¿La palabra "+str(palabra)+" es un palindromo? "+str(palindromo(palabra)))