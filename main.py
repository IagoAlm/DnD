import json


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
    if personagem['weapon']:
        armaPers = caractArma(personagem['weapon'])
        if armaPers[1] and destreza > forca:
            bonusAtk = atributos[destreza]
        else:
            bonusAtk = atributos[forca]

    if personagem['armor']:
        armdPerson = caracArmd(personagem['armor'])
    if personagem['shield']:
        escudPerson = personagem['shield']


personagem1 = abrirArq("char-warren.json")
armas = abrirArq("weapons.json")
armaduras = abrirArq("armor.json")
atributos = abrirArq("attributes.json")


atrPersonagem(personagem1)
