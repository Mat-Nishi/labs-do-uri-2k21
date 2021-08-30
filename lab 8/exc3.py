import csv
produtos = {0: [44, 'Parafuso', '', '2.10', ''],
            1: [11, 'Prego', '', '0.90', ''],
            2: [22, 'Porca', '', '0.50', ''],
            3: [33, 'Bucha', '', '0.10', '']
            }
with open("produtos.csv", 'w', newline="") as arq:
    writer = csv.writer(arq)
    writer.writerow(('Código', 'Descrição', 'Quantidade', 'Preço', 'Total'))
    for i in range(4):
        qtd = int(input())
        produtos[i][2] = qtd
        produtos[i][4] = qtd*float(produtos[i][3])
        linha = (produtos[i][0], produtos[i][1], produtos[i]
                 [2], produtos[i][3], f'{produtos[i][4]:.2f}')
        writer.writerow(linha)