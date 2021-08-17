# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 19:44:10 2021

@author: Mateus
"""

# Conjunto de funções para uma calculadora.


def soma(x, y):
    resultado = x+y
    return resultado


def subtracao(x, y):
    resultado = x-y
    return resultado


def multiplicacao(x, y):
    resultado = x*y
    return resultado


def divisao(x, y):
    resultado = x/y if y else None
    return resultado


def exponenciacao(x, y):
    if (x == 0 and y < 0) or type(y) != int:
        resultado = None
    else:
        resultado = x**y

    return resultado


def somasRec(N, denominador, ciclo):
    if N == ciclo:
        return 0
    else:
        return (((-1)**N)/denominador) + somasRec(N+1, denominador+2, ciclo)


def pi(N):
    if N < 0 or type(N) != int:
        return None
    elif N == 0:
        return 0
    else:
        return float(4*(1 + somasRec(1, 3, N)))


def fatorial(x):
    if x < 0 or type(x) != int:
        return None
    elif x == 0 or x == 1:
        return 1
    else:
        return x*fatorial(x-1)


def permutacao(n, p):
    if n >= 0 and type(n) == int and p <= n and p >= 0 and type(p) == int:
        resultado = fatorial(n)/fatorial(n-p)
    else:
        resultado = None

    return int(resultado)


def combinacao(n, p):
    if n >= 0 and type(n) == int and p <= n and p >= 0 and type(p) == int:
        resultado = fatorial(n)/(fatorial(n-p)*fatorial(p))
    else:
        resultado = None

    return int(resultado)


def somatorio(i, f):
    if type(i) == int and type(f) == int:
        resultado = sum(range(i, f+1))
    else:
        resultado = None

    return resultado


def exp(x):
    soma = 0
    for i in range(100):
        soma += (x**i)/fatorial(i)

    if soma == 1:
        soma = int(soma)

    return soma


def ln(x):
    if x > 0:
        soma = 0
        for i in range(100):
            soma += (1/((i*2)+1))*(((x-1)/(x+1))**(i*2))

        resultado = 2*((x-1)/(x+1))*soma

    else:
        resultado = None

    return resultado


def superExponenciacao(x, y):
    if x > 0:
        resultado = exp(y*ln(x))
    else:
        resultado = None

    return resultado


def raizQuadrada(x):
    if x >= 0:
        # resultado = x**(0.5) ou
        resultado = superExponenciacao(x, 0.5)
    else:
        resultado = None

    return resultado
