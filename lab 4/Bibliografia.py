nome = list(input().split())

saida = str(nome[-1]) + ', '
for i in range(len(nome)-1):
    saida += str(list(nome[i])[0])
    saida += '. '

print(saida[:-1].upper())