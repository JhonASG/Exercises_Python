# Ingreso de los datos x el usuario
cad = (input("Ingresa un string: ")).lower()
# Array de vocales
vowel = ["a", "e", "i", "o", "u"]

if cad[0] in vowel:
	print("True")
else:
	print("False")