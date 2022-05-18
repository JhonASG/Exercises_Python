cad = input()
palabra = ""
lista = []

#Forma extensa
'''
for i in range (len(cad)):
    if cad[i] != " " and i != len(cad)-1:
        palabra += cad[i]
    else:
        lista.append(palabra)
        palabra = ""

print(lista)
'''
#Una forma más sencilla utilizar split
lista2 = cad.split(' ')
print(lista2)
