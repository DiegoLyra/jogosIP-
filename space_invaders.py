status = {'Movimentações':0, 'Disparos':0, 'Abatimentos':0}
l = 37
c = 20

def menu():
    print("0 - Encerrar\n1 - Mover\n2 - Disparar\nEscolha uma das opções do menu: ")

def verificar(opcao, possiveis):
    if not opcao in possiveis:
        opcao = int(input("Entrada inválida. Digite novamente.\n"))
    return opcao

def mover(mov):
    global l, c
    if mov == 4 and c > 0:
        matriz[l][c-1] = matriz[l][c]
        matriz[l][c] = '   '
        c -= 1
        status['Movimentações'] += 1
    elif mov == 6 and c < 39:
        matriz[l][c+1] = matriz[l][c]
        matriz[l][c] = '   '
        c += 1
        status['Movimentações'] += 1
    imprimir_matriz(matriz)
    digito = int(input('2 - Encerrar movimentação\n8 - Efetuar disparo\nEscolha a direção: '))
    digito = verificar(digito, (8,2))
    if digito == 8:
        disparar()

def disparar():
    global l, c, status
    status['Disparos'] += 1
    for i in range (36, -1, -1):
        if matriz[i][c] == " W ":
            print("Acertou um inimigo!")
            matriz[i][c] = '   '
            status['Abatimentos'] += 1
            return
        elif matriz[0][c] == '   ':
            print("Atirou no ar!")
            return

def aliens():
    global contador, x
    for i in range(36, 0, -1):
        for j in range(40):
            matriz[i][j] = matriz[i-1][j]
    if contador % 2 == 0:
        matriz[0] = par()  
    else: 
        matriz[0] = impar()
    contador += 1
    if contador == 37:
        print("Fim de Jogo")
        for chave, valor in status.items():
            print("{}:{}".format(chave, valor))
        x = 0

def par():
    ET = []
    for i in range(20):
        x = ' W '
        y = '   '
        ET.append(y)
        ET.append(x)
    return ET

def impar():
    ET = []
    for i in range(20):
        x = ' W '
        y = '   '
        ET.append(x)
        ET.append(y)
    return ET

def imprimir_matriz(mtz):
    for linha in mtz:
        print(*linha)
    return mtz

matriz = []
for i in range (40):
    linha = []
    for j in range(40):
        o = '   '
        linha.append(o)
    matriz.append(linha)
matriz [37][20] = "/|\\"
matriz [0] = par()

for i in range (40):
    matriz [38][i] = '###'
    matriz [39][i] = '###'

imprimir_matriz(matriz)
contador = 1
x = 1
while x != 0:
    menu()
    entrada = int(input())
    entrada = verificar(entrada, (0,1,2))
    if entrada == 1:
        imprimir_matriz(matriz)
        y = 2
        while y == 2:
            print("4 - Mover para a esquerda\n6 - Mover para a direita\nEscolha a direção: ")
            movimentacao = int(input())
            movimentacao = verificar(movimentacao, (4,6))
            mover(movimentacao)
            y = 1
        aliens()
    elif entrada == 2:
        disparar()
        aliens()
        imprimir_matriz(matriz)
    else:
        print("Pediu arrego!")
        for chave, valor in status.items():
            print("{}:{}".format(chave, valor))
        x = 0
