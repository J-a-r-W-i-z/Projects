import cv2

pic=cv2.imread('Level1.png',0)

for j in range(7):
    for i in pic[j]:
        print(chr(i),end="")




