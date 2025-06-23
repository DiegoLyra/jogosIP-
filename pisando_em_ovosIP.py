def menu():
    print("1 - Definir Armador")
    print("2 - Plantar Armadilhas")
    print("3 - Iniciar como Andarilho")
    print("4 - Mostrar o placar")
    print("0 - Finalizar o jogo")

def verificar(possivel_entrada, opcao):
    while opcao not in possivel_entrada:
        opcao = int(input("Entrada inválida. Digite uma nova entrada\n"))
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
    global pontos_and, pontos_arm
    while x < 5:
        andar = int(input("São validos os espaços:{}\nEscolha sabiamente um dos espaços válidos\n".format(possibilidades)))
        andar-= 1
        possibilidades = (0,1,2,3,4)
        andar = verificar(possibilidades, andar)
        if ter[x][andar] == "O":
            print("Eca! Você pisou em um ovo podre e perdeu")
            pontos_arm += 1
            return
        elif andar == 0:
            possibilidades = (1,2)
            andar = verificar(possibilidades, andar)
        elif andar == 4:
            possibilidades = (4,5)
            andar = verificar(possibilidades, andar)
        else:
            possibilidades = [andar, andar+1, andar+2]
            andar = verificar(possibilidades, andar)
        x += 1
    print("Você atravessou o terreno sem cair em nenhuma armadilha! Parabéns!!!")
    pontos_and += 1

andarilho = 0
armador = 0
pontos_and = 0
pontos_arm = 0
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
        andarilho = 2 if armador == 1 else 1
        print("O armador é o jogador: {} \nO andarilho é o jogador: {}".format(armador, andarilho))
    elif entrada == 2:
        if armador == 0 or andarilho == 0:
            print("Primeiro, defina os jogadores")
        else:
            print("O terreno base é: ")
            ter = terreno()
            for linha in ter:
                print(*linha)
            plantar_armadilhas()
            for linha in ter:
                print(*linha)
    elif entrada == 3:
        if armador == 0 or andarilho == 0:
            print("Primeiro, defina os jogadores")
        else:
            for x in range(100):
                print("=" * x)
            linha = 0
            espacos = [1,2,3,4,5]
            andar_andarilho(linha, espacos)
    elif entrada == 4:
        print("Pontuação do jogador {}: {}".format(andarilho, pontos_and))
        print("Pontuação do jogador {}: {}".format(armador, pontos_arm))
    menu()
    entrada = int(input())
