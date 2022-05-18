email = input()
cont = 0

for i in email:
    if i == '@' or i == '.':
        cont += 1

if cont == 2:
    print("¡Es válido!")
else:
    print("¡No es válido!")