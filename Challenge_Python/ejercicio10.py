'''
#Primera solución
def procedimiento(cad,x):
    NewCad = str()
    for y in range(0, int(cad[x])):
        NewCad += '*'
    return NewCad

ListNum = [4,9,7]
print("El histograma es: "+'\n')
i = 0
x = 0
while i < len(ListNum):
    print(procedimiento(ListNum,x))
    i += 1
    x += 1
'''
#Otra alternativa más simple
def procedimiento(cad):
    NewCad = str()
    for y in cad:
        NewCad = '*' * y
        print(NewCad)

ListNum = [4,9,7]
print("El histograma es: "+'\n')
procedimiento(ListNum)