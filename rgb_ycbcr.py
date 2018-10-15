import numpy as np

def rgb_para_ycbcr(imagem):

# Y = 0.257R´ + 0.504G´ + 0.098B´ + 16
# Cb = -0.148R´ - 0.291G´ + 0.439B´ + 128
# Cr = 0.439R´ - 0.368G´ - 0.071B´ + 128

# R´ = 1.164(Y - 16) + 1.596(Cr - 128)
# G´ = 1.164(Y - 16) - 0.813(Cr - 128) - 0.392(Cb - 128)
# B´ = 1.164(Y - 16) + 2.017(Cb - 128)

# img[i, j, 0]  #pixel da matriz azul
# img[i, j, 1]  #pixel da matriz verde
# img[i, j, 2]) #pixel da matriz vermelha

    height, width, channels = imagem.shape

# crio matrizes vazias
    imagemY = np.zeros((height, width), dtype=np.int8)
    imagemCb = np.zeros((height, width), dtype=np.int8)
    imagemCr = np.zeros((height, width), dtype=np.int8)

# preencho usando o que foi estabelecido
    imagemY = (0.114 * imagem[:, :, 0] + 0.587 * imagem[:, :, 1] + 0.299 * imagem[:, :, 2])
    imagemCr = (0.713 * imagem[:, :, 2] - 0.713 * imagemY + 128)
    imagemCb = (0.564 * imagem[:, :, 0] - 0.564 * imagemY + 128)

    imagem[:, :, 0] = imagemY
    imagem[:, :, 1] = imagemCr
    imagem[:, :, 2] = imagemCb
