# Aluno: Guilherme Braga Pinto
# 17/1062290

import numpy as np
import cv2
import copy

from rgb_ycbcr import rgb_para_ycbcr
from ycbcr_rgb import ycbcr_para_rgb
from normalized_cross_corelation import correlation

# leio a imagem final
imagem_de_trabalho = cv2.imread("imagem_final.bmp")

# passo para YCbCr
imagem_ycbcr = copy.copy(imagem_de_trabalho)
rgb_para_ycbcr(imagem_ycbcr)

# retiro o que necessito
altura, largura, channels = imagem_ycbcr.shape

# retorno que tudo deu certo
print("Imagem lida com sucesso!")

# Recortaremos da imagem um exemplo de avião
# Fui no Paint e escolhi as coordenadas de um avião, no meu caso, o segundo avião da esquerda para a direita

# a primeira coordenada representa o canto inferior direito da imagem
# a segunda coordenada representa o canto superior esquerdo
# a linha reta entre essas duas coordenadas será a diagonal da imagem

aviao_exemplo = imagem_ycbcr[601:610, 521:504, 0]
altura_aviao, largura_aviao, channels_aviao = imagem_ycbcr.shape

for y in range(altura):
    for x in range(largura):
        k = correlation(imagem_ycbcr[y:y+altura_aviao, x:x+largura_aviao], aviao_exemplo, altura_aviao, largura_aviao)
        print(k)
