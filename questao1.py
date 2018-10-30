# Aluno: Guilherme Braga Pinto
# 17/0162290

import numpy as np
import cv2
import glob
import copy
import os

from rgb_ycbcr import rgb_para_ycbcr
from ycbcr_rgb import ycbcr_para_rgb
from pixel_vizinho import pega_pixel
from filtragem_Notch import Notch_Filter

# Este é o endereço do meu diretório de imagens quando estava trabalhando no código na minha máquina com Windows 10
# este caminho deverá ser atualizado para ser rodado em outro PC, com o caminho onde as imagens se encontram
path="C:\\Users\\Guilherme Braga\\Desktop\\trab2\\ipi2\\*.bmp"

# leio todas as imagens
array_imagens = [cv2.imread(file) for file in glob.glob(path)]
numero_imagens = len(array_imagens)
altura, largura, channels = array_imagens[0].shape

# apenas para checar as imagens lidas
print("Imagens lidas: ")
print(numero_imagens)

# matriz vazia onde acumularemos os valores dos pixels
imagem_mediana = np.zeros((altura, largura), dtype = np.uint16)

# -------------------------------------------Y-------------------------------------------
# Gaussian Noise

# Passamos tudo para YCbCr e acumulamos tudo para pegarmos a média
for imagem in array_imagens:
    rgb_para_ycbcr(imagem)
    # acumulo os valores dos pixels em Y
    imagem_mediana += imagem[:, :, 0]

# Pegamos a media
imagem_mediana = imagem_mediana/numero_imagens
cv2.imwrite("imagem_media_em_Y.bmp", imagem_mediana)

# colocamos esses novos Y junto do Cb e Cr que lemos, assim voltaremos a poder ter uma imagem RGB

# media_colorida = array_imagens[0]
# media_colorida[:, :, 0] = imagem_mediana

# salvamos o auxiliar que sera juntado com as outras correções de imagens
aux_imagem = array_imagens[0]
aux_imagem[:, :, 0] = imagem_mediana

# ycbcr_para_rgb(media_colorida)
# cv2.imwrite("imagem_colorida_com_Y_medio.bmp", media_colorida)

# -------------------------------------------Cr-------------------------------------------
# corrigir ---> Crominance
# Salt and Pepper

auxiliar_com_borda = np.full((altura+2,largura+2), 255, dtype = np.uint8)
auxiliar_com_borda[1:-1, 1:-1] = aux_imagem[:, :, 2]

# molde com preto em volta para passar a mascara
# tem borda para possibilitar processamento
# se "K" é a nossa imagem e queremos passar um filtro 3x3,
# entao invadiremos a parte demarcada por "x", que agora existe arbitrariamente
# "Imagem"
#           xxx
#          xxxx
#         xxKKKKK   ...
#         xxKKKKK   ...
#         xxKKKKK   ...

# Agora pegamos a mediana

for i in range(1, largura):
    for j in range(1, altura):
        pix_medio = pega_pixel(auxiliar_com_borda, i, j)
        pix_medio.sort()
        auxiliar_com_borda[i, j] = pix_medio[4]

imagem_mediana_CR = auxiliar_com_borda[1:-1, 1:-1]
cv2.imwrite("imagem_corrigida_em_Cr.bmp", imagem_mediana_CR)

# update do auxiliar
aux_imagem[:, :, 2] = imagem_mediana_CR

#cv2.imwrite("aux_imagem_Cr.bmp", aux_imagem)
#aux_imagem_Cr = copy.copy(aux_imagem)
#ycbcr_para_rgb(aux_imagem_Cr)
#cv2.imwrite("imagem_colorida_com_Cr_corrigido.bmp", aux_imagem_Cr)

# -------------------------------------------Cb-------------------------------------------
# corrigir ---> Crominance
# Frequencia indesejada

# Transformada de Fourier no Cb em 2 dimensões, por isso o .fft2
imagem_Fourier = np.fft.fft2(aux_imagem[:, :, 1])
# Mudamos o componente de frequência 0 para o centro do espectro
imagem_Fourier_trocada = np.fft.fftshift(imagem_Fourier)

# espectro = 26 * np.log(np.abs(imagem_Fourier_trocada))
# cv2.imwrite("freq.bmp",espectro)


# Filtragem Notch
imagem_Fourier_fim = Notch_Filter(imagem_Fourier_trocada, 3)
temporario = imagem_Fourier_trocada * imagem_Fourier_fim
temporario_destrocado = np.fft.ifftshift(temporario)
cb_final = np.fft.ifft2(temporario_destrocado)
cb_final = np.int8(np.abs(cb_final))

# Outra checagem, salvamos esta imagem de Cb
cv2.imwrite("CB_final.bmp", cb_final)

# Passar denovo o processo de pegar a mediana
auxiliar_com_borda[1:-1, 1:-1] = cb_final

for i in range(1, largura):
    for j in range(1, altura):
        pix_medio = pega_pixel(auxiliar_com_borda, i, j)
        pix_medio.sort()
        auxiliar_com_borda[i, j] = pix_medio[4]

aux_imagem[:, :, 1] = auxiliar_com_borda[1:-1, 1:-1]

# Agora passamos a imagem auxiliar com as devidas correções para RGB
# Salvamos a imagem como "imagem_final.bmp", a usaremos na segunda parte do trabalho
ycbcr_para_rgb(aux_imagem)
cv2.imwrite("imagem_final.bmp", aux_imagem)
print("Imagens corrigidas!")
