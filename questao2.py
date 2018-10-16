# Aluno: Guilherme Braga Pinto
# 17/1062290

import numpy as np
import cv2
import copy

from rgb_ycbcr import rgb_para_ycbcr
from ycbcr_rgb import ycbcr_para_rgb

# leio a imagem final
imagem_de_trabalho = cv2.imread("imagem_final.bmp")

# passo para YCbCr
imagem_ycbcr = copy.copy(imagem_de_trabalho)
rgb_para_ycbcr(imagem_de_trabalho)

# retiro o que necessito
altura, largura, channels = imagem_ycbcr.shape

# retorno que tudo deu certo
print("Imagem lida com sucesso!")

aviao_exemplo =
