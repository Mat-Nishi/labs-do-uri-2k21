lin = int(input())
col = int(input())
grid = []

for l in range(lin):
    novaLinha = []
    for c in range(col):
        novaLinha.append((col*l)+c+1)
    grid.append(novaLinha)

for i in range(lin):
    print(*grid[i])
