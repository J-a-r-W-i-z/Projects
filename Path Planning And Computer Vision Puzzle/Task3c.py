import numpy
import cv2

small_image = cv2.imread('zuck2.png',-1)
large_image = cv2.imread('zucky_elon.png',-1)

w=150
h=200
res=cv2.matchTemplate(large_image,small_image,cv2.TM_CCOEFF_NORMED)
threshold=0.8
loc=numpy.where(res>=threshold)

for pt in zip(*loc[::-1]):
    print(pt)
    break
# cv2.imshow('2',large_image)
# cv2.imshow('1',small_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




