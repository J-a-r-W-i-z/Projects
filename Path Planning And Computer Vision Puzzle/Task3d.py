import numpy
import cv2

image = cv2.imread('maze_lv3.png',-1)


b,g,r=cv2.split(image)


k=0
for j in range(180):
    for i in b[j]:
        if i<228:
            b[j][k]=0
        else: b[j][k]=255
        k+=1
    k=0
cv2.imwrite('Maze.png',b)

cv2.imshow('B',b)
cv2.waitKey(0)
cv2.destroyAllWindows()

