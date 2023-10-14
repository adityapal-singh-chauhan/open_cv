import cv2 as cv
import numpy as np
import sys

map = ['@','#','$','%','!','*',',','.',' ',' ',' ',' ']

img = cv.imread(sys.path[0]+"/sample.png", 1)

grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
height, width = grayed.shape[:2]
data = np.zeros((height, width))

for i in range(0, height):
    for j in range(0, width):
        print(map[int(((grayed[i][j]/255)*9))],end = ' ')
    print("")
