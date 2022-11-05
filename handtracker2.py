import cv2
import mediapipe as mp
import time
import numpy as np
import matplotlib.pyplot as plt



cap = cv2.VideoCapture(0)

#Initialize the Hands class and store it in a variable
mpHands = mp.solutions.hands 

#Set the hands function which will hold the landmarks points
hands = mpHands.Hands()

#Draw function of hands landmarks on the image
mpDraw = mp.solutions.drawing_utils

#For calculating framerate
pTime = 0
cTime = 0

#plotting


while True:
    success, img = cap.read() #Check if the video is read correctly
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Native cv2 image reading is BGR, must be turned to RGB
    results = hands.process(imgRGB) #Procceses the image in hands.process
    #print(results.multi_hand_landmarks)
    if (results.multi_hand_landmarks): #If a hand is detected
        for handLMS in results.multi_hand_landmarks: #For Hands in [Hand1, Hand2]
            for id, lm in enumerate(handLMS.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(cx, cy)
                #for x in range(21): #Draw lines on the image, commented to save computing power
                #if id==x:
                    #cv2.putText(img, str(x), (cx,cy), cv2.FONT_ITALIC, 1, (0,0,0))

            #mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS)

    #Figuere out framerate
    #cTime = time.time()
    #fps = 1/(cTime-pTime)
    #pTime = cTime

    #Display framerate on image
    #cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
