#Mi propia solución

H = int(input('H: '))
A = int(input('A: '))

if H < A:
    Excedente = A % H
else:
    Excedente = H % A

print('Excedente: '+str(Excedente))