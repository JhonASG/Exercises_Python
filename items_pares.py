lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_n = []

for i in range(0, len(lista_a)):
    if i%2 == 0:
        lista_n.append(lista_a[i])

print(lista_n)