import cv2
import numpy
from PIL import Image
from numpy.core.fromnumeric import reshape

# Read the images from the file
small_image = cv2.imread('Level1.png',-1)
large_image = cv2.imread('zucky_elon.png',-1)
flag=0
list=[]


for i in small_image[6]:
    if i[0]==58:
        flag=1
        continue
    if flag==1:
        list.append(i)
        
for i in range(7,176):
    for j in small_image[i]:
        list.append(j)

flag=0
for i in small_image[176]:
    list.append(i)
    flag=flag+1
    if flag==4:
        break

flag=0
temp=[]
final=[]
for i in list:
    temp.append(i)
    flag+=1
    if flag%200==0:
        final.append(temp)
        temp.clear()

arr=numpy.array(list)
x=arr.reshape(200,150,3)
x=cv2.cvtColor(x,cv2.COLOR_RGB2BGR)
image= Image.fromarray(x)
image.save("zuck2.png")
print(image.size)






            

        

