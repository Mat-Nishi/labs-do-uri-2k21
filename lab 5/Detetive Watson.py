while True:
    if input() == '0':
        break
    else:
        suspeitos = list(map(int, input().split()))
        maior = suspeitos.index(max(suspeitos))
        suspeitos.pop(maior)
        if suspeitos.index(max(suspeitos)) >= maior:
            print(suspeitos.index(max(suspeitos))+2)
        else:
            print(suspeitos.index(max(suspeitos))+1)
