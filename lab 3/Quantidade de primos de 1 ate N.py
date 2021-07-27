primos = []
n = int(input())
for x in range(2, n+1):
    a = True

    for i in range(2, x):
        if (x % i == 0):
            a = False
            break

    if (a):
        primos.append(x)

print('Existe(m) {} numero(s) primo(s) entre 1 e {}'.format(len(primos), n))
