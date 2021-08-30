with open(input(), 'r') as arq:
    vals = arq.read().split('\n')
    vals.pop(-1)
    impares = [int(i) for i in vals if int(i) % 2]
    pares = [int(i) for i in vals if not int(i) % 2]

with open('par.txt', 'w') as arq:
    for val in pares:
        arq.write(str(val))
        arq.write('\n')

with open('impar.txt', 'w') as arq:
    for val in impares:
        arq.write(str(val))
        arq.write('\n')