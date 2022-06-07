# Mi solución
inputTupla = ('Loki', 'Duke', 'Princesa', 'Lisa')
variables = {
    'primer_elemento': '',
    'segundo_elemento': '',
    'tercer_elemento': '',
    'cuarto_elemento': '',    
}

cont = 0

for key in variables:
    varElements = {key: inputTupla[cont]}
    variables.update(varElements)
    cont += 1

boolElement = True

while boolElement:
    elementView = input("Ingresa que elemento deseas observar: ")
    print('**********************************')
    print(variables[elementView])
    print('**********************************')
    continueView = int(input('Ingresa 1 si deseas observar otro elemento o 2 si deseas finalizar: '))
    
    if continueView == 2:
        boolElement = False

# Solución Pywombat

# primer_elemento, segundo_elemento, _, cuarto_elemento = ('Loki', 'Duke', 'Princesa', 'Lisa')