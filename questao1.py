import numpy as np
import cv2
import glob
import copy

adress = "C:\Users\Guilherme Braga\Desktop\ipi2\*.bmp"

imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImg = len(imageArray)

# pego medidas
 height, width, channels = imageArray[0].shape

# matriz vazia de base
 averageImage = np.zeros((height, width), dtype = np.uint16)
