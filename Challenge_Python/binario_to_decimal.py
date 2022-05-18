#Forma propia de resolverlo
binario = input()
longBinario = len(binario)
decimal = 0

for i in range(0, longBinario):
    if binario[(longBinario-1)-i] == "1":
        decimal += 2 ** i
        
print(decimal)

# Forma corta de resolverlo x Pywombat
'''
number = input('Número decimal:')

print('Número binario:', int(number, 2))
'''