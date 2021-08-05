n = int(input())
precos = []
for i in range(n):
    bits, gramas = input().split()
    bits = float(bits)
    gramas = int(gramas)
    precos.append(bits*(1000/gramas))

print('{:.2f}'.format(min(precos)))
