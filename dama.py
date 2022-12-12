import sys
entr1 = 'aaaaaaaaaaaa........bbbbbbbbbbbb'
entr = 'aaaaaaaaaaaa........abcdefghijkl'


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


def verMovimento(tabuleiro, linha, jogador):
    print(tabuleiro[4])
    print(tabuleiro[5])
    if jogador == 'b':
        for i in range(len(tabuleiro[linha])):
            if tabuleiro[linha][i] != ' ':
                print(tabuleiro[linha][i])
                if tabuleiro[linha-1][i-1] == '.' and i-1 >= 0:
                    print(tabuleiro[linha][i], 'yes,', i)
                if tabuleiro[linha-1][i+1] == '.' and i-1 <= 7:
                    print(tabuleiro[linha][i], 'yes,', i+2)
    """if jogador == 'a':
        for i in range(len(tabuleiro[5])):
            if tabuleiro[5][i] != ' ':
                print(tabuleiro[5][i])
                if tabuleiro[5-1][i-1] == '.' and i-1 >= 0:
                    print(tabuleiro[5][i], 'yes,', i)
                if tabuleiro[5-1][i+1] == '.' and i-1 <= 7:
                    print(tabuleiro[5][i], 'yes,', i+2)
    """


tabuleiro = lerInput(entr)
verMovimento(tabuleiro)
