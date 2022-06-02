def Fibonacci (max_number):
    serieFibonacci = [0, 1]
    if max_number > 1: 
        for i in range(0, max_number-2):
            if max_number > 2:
                serieFibonacci.append(serieFibonacci[i] + serieFibonacci[i+1])
            else:
                serieFibonacci = serieFibonacci
    elif max_number <= 0:
        serieFibonacci = []
    else:
        serieFibonacci = serieFibonacci[0]
            
    return serieFibonacci
    
cantNum = 0

while cantNum <= 0:
    cantNum = int(input("Ingresa la cantidad de números a visualizar de la serie Fibonacci: "))
    if cantNum <= 0:
        print("***********************************")
        print("Recuerda que el número debe ser entero mayor a cero")
        print("***********************************")

print("***********************************")
print(Fibonacci(cantNum))
print("***********************************")