with open(input(), 'r') as arq:
  texto = arq.read()
  print(len(texto), len(texto.split()), len(texto.split('\n'))-1)