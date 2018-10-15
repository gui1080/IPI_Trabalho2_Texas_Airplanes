# Aluno: Guilherme Braga Pinto
# 17/1062290

import numpy as np

def pega_pixel(imagem, i, j):

    pix = []

# o "append" em Python basicamente adiciona ao final da lista apenas 1 elemento por vez
# no caso, "i" e "j" são coordenadas na imagem. No programa principal, chamaos o .sort
# para organizar os elementos. Escolhemos para a analise o elemento do meio.
# pegamos apenas os vizinhos incluindo o proprio elemento [i, j]:

#  A B C    <-- X
#  D x E
#  F G H
#
#  ^
#  |
#  Y

# A = [X-1 / Y-1]
# B = [X-1 / Y]
# C = [X-1 / Y+1]
# D = [X / Y-1]
# E = [X / Y+1]
# F = [X+1 / Y-1]
# G = [X+1 / Y]
# H = [X+1 / Y+1]

    pix.append(imagem[i + 1, j - 1])
    pix.append(imagem[i, j - 1])
    pix.append(imagem[i - 1, j - 1])
    pix.append(imagem[i + 1, j])
    pix.append(imagem[i - 1, j])
    pix.append(imagem[i, j])
    pix.append(imagem[i + 1, j + 1])
    pix.append(imagem[i, j + 1])
    pix.append(imagem[i - 1, j + 1])
    return pix
