# Algoritmos e Estruturas de Dados I
# Laboratório 07 - Funções II
# Autor: Cleo Billa
# Data: 18/08/2021
# Adaptado por: Mateus Nishimura Fonseca
# Matrícula: 149379
# Data: 18/08/2021


def troca(a, b):
    return b, a


def ordena2(a, b):
    return(min(a, b), max(a, b))


def ordena3(a, b, c):
    l = sorted([a, b, c])
    return l[0], l[1], l[2]


def multiplicaLista(l):
    mult = 1
    for i in l:
        mult *= i

    return mult


def dobraLista(l):
    return [i*2 for i in l]


def removeDuplicadosLista(l):
    # return list(set(l))
    s = []
    for i in l:
        if i not in s:
            s.append(i)
    return s


def trocaLista(l):
    l[0], l[-1] = l[-1], l[0]
    return l


def contaLetra(s, letra):
    return s.lower().count(letra.lower())


def justificaDireita(s):
    s = list(s)
    for i in range(70-len(s)):
        s.insert(0, ' ')
    return "".join(s)


def trocaString(s1, s2, s3):
    return s1.replace(s2, s3)
