texto = input()
if texto.strip() == texto[::-1].strip():
    print("'{}' eh palindromo".format(texto))
else:
    print("'{}' nao eh palindromo".format(texto))
