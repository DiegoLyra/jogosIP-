def menu():
    print("1 - Definir Armador")
    print("2 - Plantar Armadilhas")
    print("3 - Iniciar como Andarilho")
    print("4 - Mostrar o placar")
    print("0 - Finalizar o jogo")

def verificar(possivel_entrada, opcao):
    while opcao not in possivel_entrada:
        opcao = int(input("Entrada inválida. Digite uma nova entrada\n"))
    if opcao == 2 or opcao == 3:
        if armador == 0 or andarilho == 0:
            opcao = int(input("Primeiro, defina os jogadores\n"))
    return opcao

def terreno():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append("A")
        matriz.append(linha)
    return matriz

def plantar_armadilhas():
    global ter
    print("Jogador {}, você pode esconder até 3 ovos podres por linha do terreno.".format(armador))
    for i in range(5):
        qnt = int(input("Quantos ovos você deseja esconder na linha {}?\n".format(i+1)))
        qnt = verificar((1,2,3), qnt)
        for j in range(qnt):
            coluna = int(input("Em qual coluna da linha {} você quer esconder os ovos?\n".format(i+1)))
            coluna -= 1
            coluna = verificar((0,1,2,3,4), coluna)
            ter[i][coluna] = "O"
    return qnt, coluna

def andar_andarilho(x, possibilidades):
    andar = int(input("São validos os espaços:{}\nEscolha sabiamente um dos espaços válidos\n".format(possibilidades)))
    andar = verificar(possibilidades, andar)
    possibilidades = [0,1,2,3,4]
    while x < 5:
        andar-= 1
        if ter[x][andar] == "O":
            print("Eca! Você pisou em um ovo podre e perdeu")
            placar(armador)
            return
        elif andar == 0:
            possibilidades = [1,2]
        elif andar == 4:
            possibilidades = [4,5]
        else:
            possibilidades = [andar, andar+1, andar+2]
        andar = int(input("São validos os espaços:{}\nEscolha sabiamente um dos espaços válidos\n".format(possibilidades)))
        andar = verificar(possibilidades, andar)
        x += 1
    print("Você atravessou o terreno sem cair em nenhuma armadilha! Parabéns!!!")
    placar(andarilho)
    return possibilidades

def placar(personagem):
    if personagem == jogador1['numero']: 
        jogador1['pontos'] += 1
    else:
        jogador2['pontos'] += 1

jogador1 = {'numero' : 1, 'pontos': 0}
jogador2 = {'numero' : 2, 'pontos': 0}
andarilho = 0
armador = 0
coluna = 0
ter = []

menu()
entrada = int(input())
entrada = verificar((0,1,2,3,4), entrada)
while entrada != 0:
    if entrada == 1:
        selecao = int(input("Qual jogador plantará as armadilhas?\n"))
        selecao = verificar((1,2), selecao)
        armador = selecao
        andarilho = jogador2["numero"] if armador == jogador1['numero'] else jogador1['numero']
        print("O armador é o jogador: {} \nO andarilho é o jogador: {}".format(armador, andarilho))

    elif entrada == 2:
        print("O terreno base é: ")
        ter = terreno()
        for linha in ter:
            print(*linha)
        plantar_armadilhas()
        for linha in ter:
            print(*linha)

    elif entrada == 3:
        for x in range(100):
            print("=" * x)
        linha = 0
        espacos = andar_andarilho(0, [1,2,3,4,5])

    elif entrada == 4:
        print("Pontuação do jogador {}: {}".format(jogador1["numero"], jogador1['pontos']))
        print("Pontuação do jogador {}: {}".format(jogador2["numero"], jogador2['pontos']))
    menu()
    entrada = int(input())
