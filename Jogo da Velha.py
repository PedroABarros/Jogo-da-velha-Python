def inicio():
    jogar = 1
    while jogar != 2:
        jogar = int(input(" 1. Jogar 2. Sair: "))
        if jogar < 1 or jogar > 2:
            print("Numero invalido")
            jogar = 1
        else:
            if jogar:
                jogada()

def jogada():
    jogo_velha = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
    jogada = 0
    while ganhar(jogo_velha) == 0:
        print("Jogador ", jogada % 2 + 1)
        matriz(jogo_velha)
        linha = int(input("Linha :"))
        coluna = int(input("Coluna:"))
        if linha > 3 or linha < 1 or coluna > 3 or coluna < 1:
            print("Linha ou Coluna invalida")
        else:
            if jogo_velha[linha - 1][coluna - 1] == 0:
                if (jogada % 2 + 1) == 1:
                    jogo_velha[linha - 1][coluna - 1] = 1
                else:
                    jogo_velha[linha - 1][coluna - 1] = -1
            else:
                print("Ja foi usada")
                jogada -= 1

            if ganhar(jogo_velha):
                print("Jogador ", jogada % 2 + 1, " ganhou apos ", jogada + 1, " rodadas")

            jogada += 1

def ganhar(jogo_velha):
    for i in range(3):
        soma = jogo_velha[i][0] + jogo_velha[i][1] + jogo_velha[i][2]
        if soma == 3 or soma == -3:
            return 1

    for i in range(3):
        soma = jogo_velha[0][i] + jogo_velha[1][i] + jogo_velha[2][i]
        if soma == 3 or soma == -3:
            return 1

    diagonal1 = jogo_velha[0][0] + jogo_velha[1][1] + jogo_velha[2][2]
    diagonal2 = jogo_velha[0][2] + jogo_velha[1][1] + jogo_velha[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0

def matriz(jogo_velha):
    for i in range(3):
        for j in range(3):
            if jogo_velha[i][j] == 0:
                print(" _ ", end=' ')
            else:
                if jogo_velha[i][j] == 1:
                    print(" X ", end=' ')
                else:
                    if jogo_velha[i][j] == -1:
                        print(" O ", end=' ')

        print()

inicio()

