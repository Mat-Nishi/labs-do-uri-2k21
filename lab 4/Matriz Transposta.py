l, c = map(int, input().split())
grid = []

for x in range(l):
    grid.append(list(map(int, input().split())))

for y in range(c):
    linha = []
    for x in range(l):
        linha.append(grid[x][y])
    print(*linha)