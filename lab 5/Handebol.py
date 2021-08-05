jogadores, partidas = map(int, input().split())
time = []
cont = jogadores

for i in range(jogadores):
    gols = list(map(int, input().split()))
    for j in range(partidas):
        if gols[j] == 0:
            cont -= 1
            break

print(cont)
