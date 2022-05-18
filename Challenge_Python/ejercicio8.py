def superposicion(L1,L2):
    igualdad = 0
    for x in range(0, len(L1)):
        for y in range(0, len(L2)):
            if L1[x] == L2[y]:
                igualdad += 1
    
    if igualdad > 0:
        return True
    else:
        return False

list1 = input("Ingresa la primera lista: ")
list2 = input("Ingresa la segunda lista: ")

print("¿Hay al menos un miembro en común entre las dos listas? "+str(superposicion(list1,list2)))