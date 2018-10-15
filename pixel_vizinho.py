import numpy as np

def pega_pixel(imagem, i, j):

    pix = []

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
