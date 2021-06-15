import cv2
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vid=cv2.VideoCapture(0)

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

class object:
    def __init__(self,size=50):
        self.size=size
        self.speedx = 10
        self.speedy = 10
        self.x = 50
        self.y = 50
        self.prev_x=0
        self.prev_y=0
        self.mag=10*(2**0.5)

    def insert_object(self, frame):
        cv2.circle(frame,(self.x,self.y),self.size,(0,100,0),-1)
    
    def reflect(self,center_x,center_y,radius):   
        old_mag=(self.speedy**2+self.speedx**2)**0.5     
        coldist = radius+self.size
        nx=(center_x-self.x)/coldist
        ny=(center_y-self.y)/coldist
        p=self.speedx*nx+self.speedy*ny
        wx=self.speedx-2*p*nx
        wy=self.speedy-2*p*ny
        self.speedx=wx
        self.speedy=wy 
        new_mag=(self.speedy**2+self.speedx**2)**0.5
        self.speedx=round((old_mag*self.speedx)/new_mag)
        self.speedy=round((old_mag*self.speedy)/new_mag)


ball=object()
message= "Hi There! | Press any key to play | Press Escape key to quit"
message2= "This game is created by Anuj Kakde"
message3= "Kindly excuse the minor bugs :P  "
message4= "Try to keep your head as still as possible at the instant of collision."
message5= "You just need to give direction to the ball.  "

while(True):
    ret,frame = vid.read()
    cv2.putText(frame,message,(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),4,cv2.LINE_4)
    cv2.putText(frame,message4,(50,220),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),4,cv2.LINE_4)
    cv2.putText(frame,message5,(50,260),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),4,cv2.LINE_4)
    cv2.putText(frame,message3,(50,300),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),4,cv2.LINE_4)
    cv2.putText(frame,message2,(550,650),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2,cv2.LINE_4)
    cv2.imshow('Face Detection Game', frame)
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break
    ball.x=50
    ball.y=50
    ball.speedx=10
    ball.speedy=10
    while(True):
        ret,frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Ball Movement
        ball.prev_x=ball.x
        ball.prev_y=ball.y
        ball.x=ball.x+round(ball.speedx)
        ball.y=ball.y+round(ball.speedy)

        if ball.x<50:
            ball.x=50
            ball.speedx=round(-ball.speedx*1.1)
        if ball.x>=1220:
            ball.x=1220
            ball.speedx=round(-ball.speedx*1.1)
        if ball.y<50:
            ball.y=50
            ball.speedy=round(-ball.speedy*1.2)

        faces = face_cascade.detectMultiScale(gray, 1.1, 6)
        ball.insert_object(frame)

        for (x, y, w, h) in faces:
            center_x=x+w//2
            center_y=y+h//2
            radius=h//2
            cv2.circle(frame,(center_x,center_y),radius,(0,0,100),5)
            if (center_x-ball.x)*(center_x-ball.x)+(center_y-ball.y)*(center_y-ball.y)<= ((50+h//2)*(50+h//2)+10):
                ball.reflect(center_x,center_y,radius)
                ball.x=ball.prev_x
                ball.y=ball.prev_y

        frame = cv2.flip(frame, 1)
        cv2.imshow('Face Detection Game', frame)
        
        if ball.y>670:
            note = cv2.imread('note.png',-1)
            cv2.imshow('Note',note)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
            break


        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()
            break

    

        
    