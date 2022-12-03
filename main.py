import json
import random
import re
from itertools import cycle


def abrirArq(nome):
    with open(f"files//{nome}", "r", encoding="utf8") as fd:
        arq = json.load(fd)
    return arq


def caractArma(arma):
    carac = list()
    finesse = bool()
    two_hand = bool()

    if armas[arma]['damage']:
        dano = armas[arma]['damage']

    if armas[arma]['props']:
        propriedades = armas[arma]['props']
        if 'finesse' in propriedades:
            finesse = True
        if '2-hand' in propriedades:
            two_hand = True
    return (dano, finesse, two_hand)


def caracArmd(armadura):
    if armaduras[armadura]['AC']:
        acBase = armaduras[armadura]['AC']
    if armaduras[armadura]['type']:
        tipo = armaduras[armadura]['type']

    return (acBase, tipo)


def atrPersonagem(personagem):

    if personagem['strength']:
        forca = personagem['strength']
    if personagem['dexterity']:
        destreza = personagem['dexterity']
    escudPerson = personagem['shield']

    if personagem['weapon'] or personagem['weapon'] != "":
        armaPers = caractArma(personagem['weapon'])
        if armaPers[1] and destreza > forca:
            personagem['bonusAtk'] = atributos[destreza]
            personagem['atrBonus'] = 'Destreza'

        else:
            personagem['bonusAtk'] = atributos[forca]
            personagem['atrBonus'] = 'Força'
        personagem['dadoArma'] = armaPers[0]

    if personagem['armor']:
        armdPerson = caracArmd(personagem['armor'])
        classArmd = armdPerson[0]

        if armdPerson[1] == 'light':
            classArmd = classArmd + atributos[destreza]
        elif armdPerson[1] == 'medium':
            if atributos[destreza] >= 2:
                classArmd = classArmd + 2
            elif atributos[destreza] < 2:
                classArmd = classArmd + atributos[destreza]

        if not armaPers[2] and escudPerson:
            classArmd = classArmd + 2
        personagem['CA'] = classArmd

    return personagem


def combate(personagem1, personagem2):

    i = 0
    atk = ''
    defe = ''
    danoArma = int()
    ordem = list()

    if personagem1['dexterity'] > personagem2['dexterity']:
        ordem = (personagem1, personagem2)
    elif personagem1['dexterity'] < personagem2['dexterity']:
        ordem = (personagem2, personagem1)

    ciclo = cycle([0, 1])

    while personagem1['HP'] > 0 and personagem2['HP'] > 0:

        contr = next(ciclo)

        if contr == 0:
            atk = ordem[0]
            defe = ordem[1]
        elif contr == 1:
            atk = ordem[1]
            defe = ordem[0]

        print(f"\n--Turno de ataque de {atk['name']}--")
        acerto = random.randint(1, 20) + atk['bonusAtk']
        print(
            f"O dado de acerto foi {acerto} ({acerto - atk['bonusAtk']} + {atk['bonusAtk']} de {atk['atrBonus']})")
        print(f"Contra a classe de armadura {defe['CA']} de {defe['name']}")

        if acerto > defe['CA']:
            print(
                f"O ataque de {atk['name']} em {defe['name']} foi bem sucedido")
            danoArma = int(re.sub('[^0-9]', '', atk['dadoArma']))

            dano = random.randint(1, danoArma) + atk['bonusAtk']
            print(
                f"O dano aplicado foi {dano} ({dano - atk['bonusAtk']} + {atk['bonusAtk']} de {atk['atrBonus']})")

            defe['HP'] = defe['HP'] - dano
            print(f"A vida restante do {defe['name']} é de {defe['HP']}")
        else:
            print(f"O ataque de {atk['name']} em {defe['name']} falhou")

    if personagem1['HP'] <= 0:
        print(
            f"\nO vencedor do combate foi {personagem2['name']} com {personagem2['HP']} de vida")
    elif personagem2['HP'] <= 0:
        print(
            f"\nO vencedor do combate foi {personagem1['name']} com {personagem1['HP']} de vida")


ficha1 = abrirArq("char-warren.json")
ficha2 = abrirArq("char-teste.json")

armas = abrirArq("weapons.json")
armaduras = abrirArq("armor.json")
atributos = abrirArq("attributes.json")

combate(atrPersonagem(ficha1), atrPersonagem(ficha2))
