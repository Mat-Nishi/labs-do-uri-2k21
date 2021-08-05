n = int(input())
for i in range(n):
    instrucoes = int(input())
    movimentos = []
    for i in range(instrucoes):
        instrucao = input()
        if instrucao == 'LEFT':
            movimentos.append(-1)
        elif instrucao == 'RIGHT':
            movimentos.append(1)
        else:
            idx = int(instrucao.split()[-1]) - 1
            movimentos.append(movimentos[idx])
    print(sum(movimentos))
