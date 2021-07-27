lista = []
for i in range(4):
    lista.append(float(input()))
media = sum(lista)/4

if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Exame')
else:
    print('Reprovado')
