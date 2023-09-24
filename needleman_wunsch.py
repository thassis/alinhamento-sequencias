import numpy as np


class Direcao:
    DIAGONAL = 0
    ESQUERDA = 1
    CIMA = 2
    NENHUMA = 3


class Celula:
    score = 0
    direcao = Direcao.NENHUMA


def print_matriz(matriz, seq_v, seq_w):
    spaces = 5

    def get_direcao(direcao):
        if direcao == Direcao.DIAGONAL:
            return "\\"
        elif direcao == Direcao.ESQUERDA:
            return "_"
        elif direcao == Direcao.CIMA:
            return "|"
        else:
            return ""

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] is not None:
                value = str(matriz[i][j].score) + get_direcao(matriz[i][j].direcao)
                spaces_to_add = " " * (spaces - len(value))
                print(value + spaces_to_add, end=" ")
            else:
                print("None", end=" ")
        print()


def inicializa_matriz(seq_v, seq_w):
    matriz = np.empty((len(seq_v) + 1, len(seq_w) + 1), dtype=Celula)
    for i in range(len(seq_v) + 1):
        matriz[i][0] = Celula()

    for j in range(len(seq_w) + 1):
        matriz[0][j] = Celula()

    return matriz


def needleman_wunsch(seq_v, seq_w, matriz_substituicao, penalidade_gap=0):
    matriz = inicializa_matriz(seq_v, seq_w)

    for i in range(1, len(seq_v) + 1):
        for j in range(1, len(seq_w) + 1):
            matriz[i][j] = Celula()

            score_esquerda = matriz[i][j - 1].score + penalidade_gap
            score_cima = matriz[i - 1][j].score + penalidade_gap
            score_diagonal = (
                matriz[i - 1][j - 1].score
                + matriz_substituicao[seq_v[i - 1]][seq_w[j - 1]]
            )

            if score_diagonal >= score_esquerda and score_diagonal >= score_cima:
                matriz[i][j].score = score_diagonal
                matriz[i][j].direcao = Direcao.DIAGONAL
            elif score_esquerda >= score_cima:
                matriz[i][j].score = score_esquerda
                matriz[i][j].direcao = Direcao.ESQUERDA
            else:
                matriz[i][j].score = score_cima
                matriz[i][j].direcao = Direcao.CIMA

    print_matriz(matriz, seq_v, seq_w)
