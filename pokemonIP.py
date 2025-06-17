import random

def menu():
    print("Bem-Vindo!\nA qualquer momento você pode escolher uma das opções:")
    print("9 - Para abrir esse menu\n8 - Subir\n2 - Descer\n4 - Ir para a esquerda\n6 - Ir para a direita\n5 - Abrir Pokedex\n0 -  Sair do jogo")

def mostrar_pokedex():
    global pokedex
    print(pokedex.keys())
    digito = 1
    while digito != 0:
        digito = input("Digite\n1 para Listar Detalhes\n2 para Apagar Registro\n0 para voltar ao Menu Principal\n")
        digito = int(verificar_acao(digito, ('1','2','0')))
        if digito == 1:
            nome_pokemon = input("Digite o nome do pokemon que você deseja ver detalhes:")
            nome_pokemon = verificar_acao(nome_pokemon, pokedex.keys())
            print(pokedex[nome_pokemon])
        elif digito == 2:
            nome_pokemon = input("Digite o nome do pokemon que você deseja apagar:")
            pokedex[nome_pokemon] = {}
        
    return digito, nome_pokemon

def pokemon_apareceu():
    global pokedex, entrada
    if random.choice([True, False]) == True:
        especie = random.choice(especies)
        print("Um pokemon selvagem apareceu!")
        escolha = input("Capturar ou correr? [1-Capturar ou 2-Correr]: ")
        escolha = int(verificar_acao(escolha, ('1', '2')))
        if escolha == 1:
            if especie in pokedex:
                print("{} já foi capturado antes!".format(especie))
            else:
                pokedex [especie] = {
                    "HP": random.randint(0, 100),
                    "Atk": random.randint(0, 100),
                    "Def": random.randint(0, 100),
                    "Sp. Atk": random.randint(0, 100),
                    "Sp. Def": random.randint(0, 100),
                    "Speed": random.randint(0, 100)
                }
                print("{} foi capturado com sucesso!".format(especie))
                if len(pokedex) == len(especies):
                    print("Parabéns! Você completou a pokedex.")
                    entrada == 0
        else:
            print("Fujão")
        return especie, escolha

def mapa(l, c):
    matriz = [
    ['A','A','A','A','A',' ',' ','A','A','A','A','A'],
    ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
    ['A',' ',' ',' ','A',' ',' ',' ',' ',' ',' ','A'],
    ['A','E','E','E','A','E','E','E','G','G','G','A'],
    ['A',' ',' ',' ','A','E','E','E','G','G','G','A'],
    ['A','E','E','E','A','G','G','G','G','G','G','A'],
    ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
    ['A',' ',' ',' ',' ',' ',' ',' ','G','G','G','A'],
    ['A','A','E','E','E','A','A','A','G','G','G','A'],
    ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
    ['A','E',' ','E','E',' ','E','E','E','E','E','A'],
    ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
    ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
    ['A','A','A','A','A','A','G','G','G','E','E','A'],
    ['A',' ',' ',' ',' ',' ','G','G','G',' ',' ','A'],
    ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
    ['A','E','E',' ',' ','E','E','E','E','E','E','A'],
    ['A',' ','G','G','G','G',' ',' ','G','G','G','A'],
    ['A','G','G','G',' ',' ',' ','G','G',' ',' ','A'],
    ['A','A','A','A','A','A','G','A','A','A','A','A']
    ]
    
    matriz[l][c] = 'J'
    for linha in matriz:
        print(*linha)
    return matriz 

def posicao(acao):
    global x, y
    if acao == 8:
        x -= 1
    elif acao == 2:
        x += 1
    elif acao == 4:
        y -= 1
    elif acao == 6:
        y += 1
    verificar_mapa(entrada)
    print("Sua posição atual é: [{}][{}]".format(x,y))
    mapa(x,y)
    

def verificar_acao(acao, possivelAcao):
    while acao not in possivelAcao:
        acao = input("AÇÃO INVÁLIDA. Digite novamente:\n")
    return acao
    
def verificar_mapa(acao):
    global x, y
    if terreno[x][y] == 'E' or terreno[x][y] == 'A':
        print('BUMP!')
        if acao == 4:
            y += 1
        if acao == 6:
            y -= 1
        if acao == 8:
            x += 1
        if acao == 2:
            x -= 1
    if terreno[x][y] == 'G':
        pokemon_apareceu()
    return acao

entrada = 1
x = 19
y = 6
especies = ["Ratata", "Pidgey", "Weedle", "Caterpie", "Paras", "Charmander", "Bulbasaur", "Squirtle", "Pikachu", "Evee"]
pokedex = {}


menu()
print("Entrando na Rota 1")
terreno = mapa(x,y)
print("Sua posição atual é: [{}][{}]".format(x,y))
while entrada != 0:
    entrada = input()
    entrada = int(verificar_acao(entrada, ('0','2','4','5','6','8','9')))
    if entrada == 9:
        menu()
        entrada = int(input())
    elif entrada == 5:
        mostrar_pokedex()
        mapa(x,y)
    else:
        posicao(entrada)
