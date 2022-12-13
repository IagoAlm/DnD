import sys
import string
entr1 = 'aaaaaaaaaaaa........bbbbbbbbbbbb'
entr = 'aaaaaaaa......B.....acbdefghijkl'


def lerInput(entrada):
    linha = list()
    tabuleiro = list()
    coluna = 1
    contr = 0
    fileira = 1
    for i in range(0, len(entrada)*2, 1):
        if fileira % 2 != 0:
            if coluna % 2 == 0:
                linha.append(entrada[contr])
                contr += 1
            else:
                linha.append(' ')

        elif fileira % 2 == 0:
            if coluna % 2 != 0:
                linha.append(entrada[contr])
                contr += 1
            else:
                linha.append(' ')

        if coluna < 8:
            coluna = coluna + 1
        else:
            tabuleiro.append(linha)
            linha = []
            coluna = 1
            fileira = fileira + 1
    return tabuleiro


def verAcima(tabuleiro, linha, i):
    if tabuleiro[linha-1][i-1] == '.' and i-1 >= 0:

        esquerdaInt = str(linha+1)
        esquerdaInt = esquerdaInt + str(i-1)
        #esquerdaInt = esquerdaInt + list(string.ascii_lowercase)[i-1]
    if tabuleiro[linha-1][i+1] == '.' and i-1 <= 7:
        direitaInt = str(linha+1)
        direitaInt = direitaInt + str(i+1)
        #direitaInt = direitaInt + list(string.ascii_lowercase)[i+1]
    # o retorno desses dados é 1 a mais na linha
    return (esquerdaInt, direitaInt)


def verAbaixo(tabuleiro, linha, i):
    if tabuleiro[linha+1][i-1] == '.' and i-1 >= 0:

        esquerdaInt = str(linha+2)
        #esquerdaInt = esquerdaInt + list(string.ascii_lowercase)[i-1]
        esquerdaInt = esquerdaInt + str(i-1)
    if tabuleiro[linha+1][i+1] == '.' and i-1 <= 7:
        direitaInt = str(linha+2)
        direitaInt = direitaInt + str(i+1)
    # o retorno desses dados é 1 a mais na linha
    return (esquerdaInt, direitaInt)


def verMovimento(tabuleiro, linha, jogador):
    if jogador == 'b':
        for i in range(len(tabuleiro[linha])):
            if tabuleiro[linha][i] == 'b':
                print(verAcima(tabuleiro, linha, i))
            if tabuleiro[linha][i] == 'B':
                print(verAcima(tabuleiro, linha, i))
                print(verAbaixo(tabuleiro, linha, i))

    if jogador == 'a':
        for i in range(len(tabuleiro[5])):
            if tabuleiro[linha][i] == 'a':
                print(verAcima(tabuleiro, linha, i))
            if tabuleiro[linha][i] == 'A':
                print(verAcima(tabuleiro, linha, i))
                print(verAbaixo(tabuleiro, linha, i))


tabuleiro = lerInput(entr)
print(tabuleiro)

verMovimento(tabuleiro, 5, 'b')
