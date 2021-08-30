with open("numeros.txt", 'w') as arq:
  for i in range(10):
    arq.write(input())
    arq.write('\n')