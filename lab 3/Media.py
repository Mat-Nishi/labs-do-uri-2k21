pares = []
impares = []
while(True):
    n = int(input())
    if n == 0:
        print('Pares: {} valor(es)'.format(len(pares)))
        print('Impares: {} valor(es)'.format(len(impares)))
        print('Media: {:.2f}'.format(
            (sum(pares)+sum(impares))/(len(pares)+len(impares))))
        break
    else:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
