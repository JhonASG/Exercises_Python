def vowel_counter(cad):
    vowel = ['a', 'e', 'i', 'o', 'u']
    cont = 0
    
    for letters in cad:
        if letters in vowel:
            cont += 1
    
    return cont
    

cad = input("Ingresa el texto: ").lower()

print(vowel_counter(cad))