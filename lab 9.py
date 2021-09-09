from graphics import *
from random import randint, choice
import re


def limpaJanela(janela):
    for item in janela.items[:]:
        item.undraw()
    janela.update()


def desenhaForca(janela, width, height):
    base = Line(Point(width/4 - 40, height/2 + 30),
                Point(width/4 + 40, height/2 + 30))
    poste = Line(Point(width/4, height/2 + 30),
                 Point(width/4, height/2 - 90))
    cabo = Line(Point(width/4, height/2 - 90),
                Point(width/4+40, height/2 - 90))
    corda = Line(Point(width/4+40, height/2 - 90),
                 Point(width/4+40, height/2 - 75))
    corda.draw(janela)
    cabo.draw(janela)
    poste.draw(janela)
    base.draw(janela)


def escreveForca(nivel, janela, w, h):
    if nivel == 0:
        texto = Text(Point(w-30, h), "F")
        texto.setSize(12)
        texto.setFace('helvetica')

    if nivel == 1:
        texto = Text(Point(w-15, h), "O")
        texto.setSize(12)
        texto.setFace('helvetica')

    if nivel == 2:
        texto = Text(Point(w, h), "R")
        texto.setSize(12)
        texto.setFace('helvetica')

    if nivel == 3:
        texto = Text(Point(w+15, h), "C")
        texto.setSize(12)
        texto.setFace('helvetica')

    if nivel == 4:
        texto = Text(Point(w+30, h), "A")
        texto.setSize(12)
        texto.setFace('helvetica')

    texto.draw(janela)


def main():
    height, width = 500, 1000
    janela = GraphWin("Jogo da forca", width, height)
    ops = ['+', '-', '*', '/']
    calc = ''
    pergunta = ''
    acertos = 0
    vidas = 5
    while(True):
        textoEntrada = Text(
            Point(width/2, height/2 - 40), "Selecione a quantidade de numeros (máx = 10, min = 2):")
        textoContinua = Text(
            Point(width/2, height/2 - 20), "Clique em qualquer lugar para continuar")
        entrada = Entry(Point(width/2, height/2 + 20), 10)
        textoEntrada.draw(janela)
        textoContinua.draw(janela)
        entrada.draw(janela)
        janela.getMouse()
        try:
            n = int(entrada.getText())
            n = max(2, n)
            n = min(n, 10)
            textoEntrada.undraw()
            textoContinua.undraw()
            entrada.undraw()
            break
        except:
            textoEntrada.setText(
                "Insira apenas valores numéricos")
            entrada.undraw()
            janela.getMouse()
            textoEntrada.undraw()
            entrada.undraw()
            textoContinua.undraw()

    while(True):
        vals = [randint(0, 10) for i in range(n)]
        opVals = [choice(ops) for i in range(n-1)]

        for i in range(n-1):
            calc += str(vals[i])
            calc += opVals[i]
            pergunta += str(vals[i])
            pergunta += '_'
        calc += str(vals[-1])
        pergunta += str(vals[-1])
        try:
            r = eval(calc)
            calc += f'={r}'
            pergunta += f'={r}'
            break
        except:
            continue

    desenhaForca(janela, width, height)
    mostrarPergunta = Text(Point(width/2, height - (height/3)), pergunta)
    textoTentativa = Text(
        Point(width/2, height - (height/3) + 25), "Digite seu chute e clique na tela:")
    inTentativa = Entry(Point(width/2, height - (height/3) + 60), 10)
    textoTentativa.draw(janela)
    inTentativa.draw(janela)
    mostrarPergunta.draw(janela)
    mostrarVidas = Text(Point(width-50, 30), f"Vidas: {vidas}")
    mostrarVidas.draw(janela)

    while True:
        janela.getMouse()
        chute = inTentativa.getText()
        if chute == opVals[acertos]:
            feedback = Text(Point(
                width/2, height/3), "Correto!\nClique em qualquer lugar para continuar jogando")
            feedback.draw(janela)
            janela.getMouse()
            feedback.undraw()
            pergunta = re.split('(_)', pergunta)
            pergunta[1] = opVals[acertos]
            pergunta = "".join(pergunta)
            mostrarPergunta.setText(pergunta)
            acertos += 1
        else:
            vidas -= 1
            mostrarVidas.setText(f"Vidas: {vidas}")
            feedback = Text(Point(
                width/2, height/3), "Errado!\nClique em qualquer lugar para continuar jogando")
            feedback.draw(janela)
            escreveForca(4-vidas, janela, width/4+40, height/2-70)
            janela.getMouse()
            feedback.undraw()

        if vidas == 0:
            limpaJanela(janela)
            textoFim = Text(Point(width/2, height/2),
                            "Você Perdeu!\nClique em qualquer lugar para sair")
            textoFim.draw(janela)
            break

        elif acertos == n-1:
            limpaJanela(janela)
            textoFim = Text(Point(width/2, height/2),
                            "Você Ganhou!\nClique em qualquer lugar para sair")
            textoFim.draw(janela)
            break

    janela.getMouse()
    janela.close()


if __name__ == "__main__":
    main()
