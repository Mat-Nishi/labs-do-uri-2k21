vals = []
saida = ''
for i in range(2):
    vals.append(int(input()))
vals = sorted(vals)

lista = [i for i in range(vals[0], vals[1]+1)]

for i in range(len(lista)+1):
    if i < len(lista)-1:
        saida += '{} + '.format(lista[i])
    elif i == len(lista)-1:
        saida += '{} = '.format(lista[i])
    else:
        saida += str(sum(lista))

print(saida)
