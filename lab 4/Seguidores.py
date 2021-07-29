john = []
peter = []
comum = []

nome = input()
while nome != 'fim':
    john.append(nome)
    nome = input()

nome = input()
while nome != 'fim':
    peter.append(nome)
    nome = input()

for n in john:
    if n in peter:
        comum.append(n)

for n in comum:
    peter.remove(n)
    john.remove(n)

print('Comum: {}'.format(comum))
print('John: {}'.format(john))
print('Peter: {}'.format(peter))
