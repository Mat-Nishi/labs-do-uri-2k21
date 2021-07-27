n = int(input())
a = True

for i in range(2, n):
    if (n % i == 0):
        print('{} nao eh primo!!'.format(n))
        a = False
        break

if (a):
    if (n != 1):
        print('{} eh primo!!'.format(n))
    else:
        print('{} nao eh primo!!'.format(n))
