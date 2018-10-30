# Aluno: Guilherme Braga Pinto
# 17/0162290

import numpy as np

def correlation(imagem_original, imagem_elemento, altura_aviao, largura_aviao):

    altura_1, largura_1, channels_1 = imagem_original.shape
    # altura_2, largura_2, channels_2 = imagem_elemento.shape

    soma_parcial_1 = float(np.sum(imagem_original))
    media_1 = soma_parcial_1 / (altura_1 * largura_1)
    soma_parcial_2 = float(np.sum(imagem_elemento))
    media_2 = soma_parcial_2 / (altura_aviao * largura_aviao)

    # equação de Normalized Cross Correlation
    numerador = np.sum((imagem_original - media_1) * (imagem_elemento - media_2))
    e1 = np.sum((imagem_original - media_1)**2)
    e2 = np.sum((imagem_elemento - media_2)**2)
    resultado = (numerador) / ((e1 * e2)**(1/2))
    return resultado
