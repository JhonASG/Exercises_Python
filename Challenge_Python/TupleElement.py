def printElements(t):
    inicio = list(t[0:2])
    fin = t[-1]
    inicio.append(fin)
    
    for e in inicio:
        print(e)

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

printElements(t)