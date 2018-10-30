# Aluno: Guilherme Braga Pinto
# 17/0162290 

import numpy as np

def ycbcr_para_rgb(imagem):

    height, width, channels = imagem.shape

# preenchemos a futura imagem de zeros
    imagemR = np.zeros((height, width), dtype=np.int8)
    imagemG = np.zeros((height, width), dtype=np.int8)
    imagemB = np.zeros((height, width), dtype=np.int8)

# aplicamos a equivalencia
    imagemR = imagem[:, :, 0] + (1.402 * imagem[:, :, 1] - 1.402 * 128)
    imagemG = imagem[:, :, 0] + (-0.714 * imagem[:, :, 1] - (-0.714 * 128)) + (-0.344 * imagem[:, :, 2] - (-0.344 * 128))
    imagemB = imagem[:, :, 0] + (1.772 * imagem[:, :, 2] - 1.772 * 128)

# damos overwrite
    imagem[:, :, 0] = imagemB
    imagem[:, :, 1] = imagemG
    imagem[:, :, 2] = imagemR
