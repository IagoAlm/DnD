import sys
import string
from funcDama import *
entr1 = 'aaaaaaaaaaaa........bbbbbbbbbbbb'
entr2 = 'aaaaaaaa....B.B.....acbdefghijkl'
entr = 'aaaaa...aaaa...B.aaa....efghijkl'


def jogada(tabuleiro, linha, jogador):
    if jogador == 'b':
        for i in range(len(tabuleiro[linha])):
            if tabuleiro[linha][i] == 'b':
                #print(verCapturaAcima(tabuleiro, linha, i))
                jogadasPossiveis = [x for x in verAcima(
                    tabuleiro, linha, i)]
                #print(linha+1, string.ascii_lowercase[i], " pode ir para ", tradutor(jogadasPossiveis), sep='')
            if tabuleiro[linha][i] == 'B':
                print(verCapturaAcima(tabuleiro, linha, i))
                print(verCapturaAbaixo(tabuleiro, linha, i))

                #jogadasPossiveis = [x for x in verAcima(tabuleiro, linha, i)] + [x for x in verAbaixo(tabuleiro, linha, i)]
                #print(linha+1, string.ascii_lowercase[i], " pode ir para ", tradutor(jogadasPossiveis), sep='')

    if jogador == 'a':
        for i in range(len(tabuleiro[5])):
            if tabuleiro[linha][i] == 'a':
                print(verAcima(tabuleiro, linha, i))
            if tabuleiro[linha][i] == 'A':
                print(verAcima(tabuleiro, linha, i))
                print(verAbaixo(tabuleiro, linha, i))


tabuleiro = lerInput(entr)
atualizarTabuleiro(tabuleiro)
# verQuant(tabuleiro)
#jogada(tabuleiro, 3, 'b')
