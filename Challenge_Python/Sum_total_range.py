val = True
sum = 0

while val:
    print("***************************")
    num1 = int(input("Desde: "))
    num2 = int(input("Hasta: "))
    if num1<num2:
        val = False
    else:
        val = True

for i in range(num1, num2+1):
    sum += i

print(sum)