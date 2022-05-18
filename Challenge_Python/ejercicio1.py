def mayor(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("El número mayor ingresado es "+str(mayor(num1,num2)))