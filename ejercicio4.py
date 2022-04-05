def is_vocal(caracter):
    vocales = ['a','e','i','o','u']
    if caracter.lower() in vocales:
        return True
    else:
        return False

c = input("Ingresa un caracter: ")
print("¿El caracter ingresado es una vocal? "+str(is_vocal(c)))