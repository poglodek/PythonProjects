import os
import cv2
import mediapipe 

width, height = 640, 800

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands()


camera = cv2.VideoCapture(0)
camera.set(3,width)
camera.set(4,height)

while True:
    successs, img = camera.read()
    cv2.imshow("Camera", img)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    

    if cv2.waitKey(1) == ord("q"):
        break


cv2.destroyAllWindows()