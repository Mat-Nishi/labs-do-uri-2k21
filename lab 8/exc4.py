def toMaiusculo(nomeArquivo):
    novoNome = nomeArquivo+".mais"
    with open(nomeArquivo, "r") as arq:
      texto = arq.read()
    with open(novoNome, "w") as arq:
      arq.write(texto.upper())