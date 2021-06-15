import cv2

pic=cv2.imread('treasure_mp3.png',-1)

with open("Treasure.txt", "wb") as binary_file:
    binary_file.write(pic)








