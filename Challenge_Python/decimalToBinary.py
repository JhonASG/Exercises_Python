numDecimal = int(input("Numero decimal: "))

numBinary = bin(numDecimal).replace("0b", "")

print("Numero binario: " + str(numBinary))