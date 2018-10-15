import numpy as np
import cv2
import glob
import copy
import os

from rgb_ycbcr import rgb_para_ycbcr

path="C:\\Users\\Guilherme Braga\\Desktop\\ipi2\\*.bmp"

array_imagens = [cv2.imread(file) for file in glob.glob(path)]
numero_imagens = len(array_imagens)

# teste para ver se li tudo que deveria
print(numero_imagens)

altura, largura, channels = array_imagens[0].shape
imagem_mediana = np.zeros((altura, largura), dtype = np.uint16)

for imagem in array_imagens:
    rgb_para_ycbcr(imagem)
    # acumulo os valores dos pixels em Y
    imagem_mediana = imagem_mediana + imagem[:, :, 0]

imagem_mediana = imagem_mediana/numero_imagens
