import math, random

game = 1
nick1 = ''
nick2 = ''
dic1 = {}
dic2 = {}

def menu():
    print('VERMES DE GUERRA\nEscolha uma das opções abaixo:')
    print('1 - Configurar\n2 - Iniciar partida\n0 - Sair')

def menu2():
    print('Escolha uma das opções abaixo:\n1 - Mover\n2 - Ajustar ângulo\n3 - Disparar\n4 - Encerrar turno\n')

def inteiroAleatorio(inf, sup):
    x = 0
    while x == 0:
        x = random.randint(inf, sup)
    return x

def configurar(nome1, nome2):
    global dic1, dic2
    nome1 = input("Informe o nome do jogador 1:\n")
    nome2 = input("Informe o nome do jogador 2:\n")
    dic1['Nome'] = nome1
    dic2['Nome'] = nome2
    dic1 = {
        'Nome': nome1,
        'Municao': inteiroAleatorio(10,20),
        'Ângulo': inteiroAleatorio(30,120),
        'Direção': inteiroAleatorio(-1,1),
        'Posição': inteiroAleatorio(0,69),
        'Velocidade': inteiroAleatorio(0,5),
        'Combustível': 10
        }
    dic2 = {
        'Nome': nome2,
        'Municao': inteiroAleatorio(10,20),
        'Ângulo': inteiroAleatorio(30,120),
        'Direção': inteiroAleatorio(-1,1),
        'Posição': inteiroAleatorio(0,69),
        'Velocidade': inteiroAleatorio(0,5),
        'Combustível': 10
        }
    return nome1, nome2

def verificar(opcao, possivelEscolha):
    while not opcao in possivelEscolha:
        opcao = int(input("Entrada inválida. Digite novamente."))
    return opcao

matriz = []
for i in range(6):
    linha = []
    for j in range(70):
        z = " "
        linha.append(z)
    matriz.append(linha)
for i in range(70):
    matriz[4][i] = "X"
    matriz[5][i] = "X"

def imprimir_terreno():
    for i in range(70):
        matriz[3][i] = " "
    jog1 = ">" if dic1['Direção'] == 1 else "<"
    jog2 = ">" if dic2['Direção'] == 1 else "<"
    if dic1['Posição'] != dic2['Posição']:
        matriz[3][dic1['Posição']] = jog1
        matriz[3][dic2['Posição']] = jog2
    else:
        matriz[3][dic1['Posição': inteiroAleatorio(0,69)]] = jog1
    for linha in matriz:
        print(*linha)
    return jog1, jog2

def atributos(dicionario):
    for chave, valor in dicionario.items():
        print("{}: {}".format(chave, valor))
    return chave, valor

def mover(dicionario, anda):
    global game
    if anda == 4:
        dicionario['Posição'] = dicionario['Posição'] - 1
        dicionario['Direção'] = -1
        dicionario['Combustível'] -= 1
    else:
        dicionario['Posição'] = dicionario['Posição'] + 1
        dicionario['Direção'] = +1
        dicionario['Combustível'] -= 1
    if dicionario['Combustível']-1 == 0:
        print("Você perdeu. Combustível: {}".format(dicionario['Combustível']))
        game = 2
    return anda

def ajustar_angulo(dicionario):
    angulo = int(input("Deseja aumentar [8], diminuir [2] ou trave o ângulo [0]?\n"))
    angulo = verificar(angulo, (8,2,0))
    while angulo != 0:
        angulo = int(input("Deseja aumentar [8], diminuir [2] ou trave o ângulo [0]?\n"))
        angulo = verificar(angulo, (8,2,0))
        print("Seu ângulo: {}".format(dicionario['Ângulo']))
        atributos(dicionario)
        for linha in matriz:
            print(*linha)
        if angulo == 8:
            dicionario['Ângulo'] += 1
            if dicionario['Ângulo'] > 60:
                print("Ângulo máximo. Seu ângulo: {}".format(dicionario['Ângulo']-1))
        else:
            dicionario['Ângulo'] -= 1
            if dicionario['Ângulo'] < 30:
                print("Ângulo mínimo. Seu ângulo: {}".format(dicionario['Ângulo']+1))   
    print("Ângulo travado. Seu ângulo: {}".format(dicionario['Ângulo']))

def atirar(dicionario, adversario):
    angulo_rad= math.radians(dicionario['Ângulo'])
    calculo = (200 * math.sin(2 * angulo_rad))/9.8
    dicionario['Municao'] -= 1
    if dicionario['Municao'] == 0:
        print("Você perdeu por falta de munição!")
        game = 2

    else:
        if dicionario['Direção'] == 1:
            bala = dicionario['Posição']+calculo
        else:
            bala = dicionario['Posição']-calculo
        if bala == adversario['Posição']:
            print("Você acertou {}, parabéns {}.".format(adversario['Nome'], dicionario['Nome']))
            game = 2
        elif bala == dicionario['Posição']:
            print("Você morreu.")
            game = 2
        else:
            print("Você não acertou nada!")
            return

def primeiro_jogador(dicionario, adversario):
    imprimir_terreno()
    atributos(dicionario)
    menu2()
    digito = int(input())
    digito = verificar(digito, (1,2,3,4))
    y = 1
    while y != 0:
        if digito == 1:
            andar = int(input("Deseja se mover para a esquerda [4] ou para a direita [6]?\n"))
            andar = verificar(andar, (4,6))
            mover(dicionario, andar)
            imprimir_terreno()
            menu2()
            digito = int(input())
            digito = verificar(digito, (1,2,3,4))
        elif digito == 2:
            ajustar_angulo(dicionario)
            imprimir_terreno()
            menu2()
            digito = int(input())
            digito = verificar(digito, (1,2,3,4))
        elif digito == 3:
            atirar(dicionario, adversario)
            y = 0
        else:
            print("Turno encerrado")
            y = 0 
    return andar, digito

x = 1
while x != 0:
    menu()
    entrada = int(input())
    entrada = verificar(entrada, (1,2,0))
    if entrada == 1:
        configurar(nick1, nick2)
    elif entrada == 2:
        while nick1 not in dic1['Nome']:
            entrada = int(input("Configure os personagens antes de iniciar a partida.\n"))
        if dic1['Velocidade'] > dic2['Velocidade']:
            primeiro_jogador(dic1, dic2)
            while game == 1:
                primeiro_jogador(dic2, dic1)
                primeiro_jogador(dic1, dic2)
        else:
            primeiro_jogador(dic2, dic1)
            while game == 1:
                primeiro_jogador(dic1, dic2)
                primeiro_jogador(dic2, dic1)
        entrada = int(input())
        entrada = verificar(entrada, (1,2,0))

    else:
        print("Desligando...")
        x = 0
