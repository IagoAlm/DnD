import sys
import string

# ---------------------------FUNÇÕES QUE FUNCIONAM CORRETAMENTE E NÃO PRECISA ALTERAR NADA PELO AMOR DE DEUS--------------------------------------#


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


def atualizarTabuleiro(tabuleiro):
    print('     ', end='')
    for i in range(8):
        print(string.ascii_uppercase[i], end=' ')
    i = 0
    print(end='\n\n')
    for linha in tabuleiro:
        i += 1
        print(i, end='   |')
        for item in linha:
            print(item, end='|')
        print()


def verCapturaAcima(tabuleiro, linha, i):
    capturas = dict()
    pos1 = False
    pos2 = False
    pos3 = False
    pos4 = False
    if i-1 >= 0 and tabuleiro[linha-1][i-1] == 'a':
        if i-2 >= 0 and tabuleiro[linha-2][i-2] == '.':
            pos1 = str(linha-2)
            pos1 = pos1 + str(i-2)
        if tabuleiro[linha-2][i] == '.':
            pos2 = str(linha-2)
            pos2 = pos2 + str(i)

        esq = str(linha-1) + str(i-1)
        capturas[esq] = (pos1, pos2)
    if i+1 <= 7 and tabuleiro[linha-1][i+1] == 'a':
        if tabuleiro[linha-2][i] == '.':
            pos3 = str(linha-2)
            pos3 = pos3 + str(i)

        if i+2 <= 7 and tabuleiro[linha-2][i+2] == '.':
            pos4 = str(linha-2)
            pos4 = pos4 + str(i+2)
        direit = str(linha-1) + str(i+1)
        capturas[direit] = (pos3, pos4)
    if capturas != {}:
        return capturas


def verCapturaAbaixo(tabuleiro, linha, i):
    capturas = dict()
    pos1 = False
    pos2 = False
    pos3 = False
    pos4 = False
    if i-1 >= 0 and tabuleiro[linha+1][i-1] == 'a':
        if i-2 >= 0 and tabuleiro[linha+2][i-2] == '.':
            pos1 = str(linha+2)
            pos1 = pos1 + str(i-2)
        if tabuleiro[linha+2][i] == '.':
            pos2 = str(linha+2)
            pos2 = pos2 + str(i)

        esq = str(linha+1) + str(i-1)
        capturas[esq] = (pos1, pos2)
    if i+1 <= 7 and tabuleiro[linha+1][i+1] == 'a':
        if tabuleiro[linha+2][i] == '.':
            pos3 = str(linha+2)
            pos3 = pos3 + str(i)

        if i+2 <= 7 and tabuleiro[linha+2][i+2] == '.':
            pos4 = str(linha+2)
            pos4 = pos4 + str(i+2)
        direit = str(linha+1) + str(i+1)
        capturas[direit] = (pos3, pos4)
    if capturas != {}:
        return capturas

# ---------------------------FUNÇÕES QUE FUNCIONAM CORRETAMENTE E NÃO PRECISA ALTERAR NADA PELO AMOR DE DEUS--------------------------------------#


def verAcima(tabuleiro, linha, i):
    esquerdaInt = False
    direitaInt = False
    if tabuleiro[linha-1][i-1] == '.' and i-1 >= 0:
        esquerdaInt = str(linha-1)
        esquerdaInt = esquerdaInt + str(i-1)
        #esquerdaInt = esquerdaInt + list(string.ascii_lowercase)[i-1]
    if tabuleiro[linha-1][i+1] == '.' and i-1 <= 7:
        direitaInt = str(linha-1)
        direitaInt = direitaInt + str(i+1)
        #direitaInt = direitaInt + list(string.ascii_lowercase)[i+1]
    # o retorno desses dados é 1 a mais na linha
    if esquerdaInt and direitaInt:
        return (esquerdaInt, direitaInt)
    elif direitaInt:
        return (direitaInt,)
    elif esquerdaInt:
        return (esquerdaInt,)


def verAbaixo(tabuleiro, linha, i):
    esquerdaInt = False
    direitaInt = False
    if tabuleiro[linha+1][i-1] == '.' and i-1 >= 0:
        esquerdaInt = str(linha+1)
        #esquerdaInt = esquerdaInt + list(string.ascii_lowercase)[i-1]
        esquerdaInt = esquerdaInt + str(i-1)
    if tabuleiro[linha+1][i+1] == '.' and i-1 <= 7:
        direitaInt = str(linha+1)
        direitaInt = direitaInt + str(i+1)
    # o retorno desses dados é 1 a mais na linha
    if esquerdaInt and direitaInt:
        return (esquerdaInt, direitaInt)
    elif direitaInt:
        return (direitaInt,)
    elif esquerdaInt:
        return (esquerdaInt,)


def tradutor(coordenadas):

    coordenadas = list(coordenadas)
    lista_jogadas = list()
    for item in coordenadas:

        linha = str((int(item[0]) + 1))
        coluna = string.ascii_lowercase[int(item[1])]
        traduzid = linha + coluna
        lista_jogadas.append(traduzid)
    return lista_jogadas


"""
Necessita de uma função para interpretar a saida para o usuário, estilo: 
('43', '45') para ('5d','5f') quando for "verAcima" +1 para o usuário e um filtro que passe de número (index da lista de letra para letra) 
e ('43', '45') para ('5d','5f') quando for "verAbaixo" +1 para o usuário também
"""


def verQuant(tabuleiro, letra):
    cont = 0
    for linha in tabuleiro:
        for item in linha:
            if item == letra:
                cont += 1
    print(cont)
