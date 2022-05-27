import math as mt

# Se solicita el radio del circulo
radio = float(input("Ingresa el radio del circulo: "))
# Se calcula el area del circulo
calcArea = mt.pi * mt.pow(radio, 2)
area = round(calcArea, 2)

print("El área del circulo es: ", area)