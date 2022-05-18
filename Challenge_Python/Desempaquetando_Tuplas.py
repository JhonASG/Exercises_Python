custome = (1, 5304, True, '127.0.0.1')
variables = ("valor", "puerto", "permitido", "host")
resultado = dict()

for i in range(len(custome)):
    resultado[variables[i]] = custome[i]

for clave,valor in resultado.items():
    print(clave, ": ",valor)