def desPad(vetor):
    media = sum(vetor)/len(vetor)
    vetor = [(i - media)**2 for i in vetor]
    desv = (sum(vetor)/(len(vetor)))**0.5

    return media, desv

vals = []

val = float(input())
while val >= 0:
    vals.append(val)
    val = float(input())

media, desvio = desPad(vals)
print('Media: {:.2f}'.format(media))
print('Desvio Padrao: {:.2f}'.format(desvio))
