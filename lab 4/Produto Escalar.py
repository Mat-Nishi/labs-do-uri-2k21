v1 = []
v2 = []
soma = 0

val = int(input())
while val >= 0:
    v1.append(val)
    val = int(input())

val = int(input())
while val >= 0:
    v2.append(val)
    val = int(input())

if len(v1) > len(v2):
    for i in range(len(v1) - len(v2)):
        v2.append(0)

else:
    for i in range(len(v2) - len(v1)):
        v1.append(0)

for i in range(len(v1)):
    soma += v1[i]*v2[i]

print('Produto Escalar: {}'.format(soma))