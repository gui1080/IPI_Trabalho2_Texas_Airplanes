# Aluno: Guilherme Braga Pinto
# 17/1062290

import numpy as np

def pares_filtragem_Notch(imagem, numero_pares, dzero, k, l):

    height, width, channels = imagem.shape

    HM = np.ones((height, width), dtype=np.float16)
    Hm = np.ones((height, width), dtype=np.float16)

    centro = (height/2, width/2)

    # para cada pixel ,se aplica a equação
    for i in range(height):
        for j in range(width):
            dM  = (((i - centro[0] - k)**2) + ((j - centro[1] - l)**2))**(1/2)
            dm = (((i - centro[0] + k)**2) + ((j - centro[1] + l)**2))**(1/2)

            HM[i, j] = (1/(1 + (dzero/dM)**(2*numero_pares)))
            Hm[i, j] = (1/(1 + (dzero/dm)**(2*numero_pares)))

    return Hm * HM

def Notch_Filter(imagem, numero_pares):
# frequencioa de H(u, v) deve estar a certa fração de seu máximo
# No caso, a imagem é de 720x720
# D0 = cutoff frequency, se H(u, v) = D0, então o filtro esta a 0,667 do valor máximo


    return final
