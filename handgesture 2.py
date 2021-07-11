import cvzone
import cv2
import time
import math
import numpy as np
import pyautogui as p
import time as t
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)
detector = cvzone.HandDetector(detectionCon=0.7, maxHands=2)

# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))

# volRange = volume.GetVolumeRange()

# minVol = volRange[0]
# maxVol = volRange[1]

# print(volume.GetVolumeRange())


while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img,2)

    frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    # Control Audio through fingers
    # if len(lmList) != 0:
        
    #     x1, y1 = lmList[4][1], lmList[4][2]
    #     x2, y2 = lmList[8][1], lmList[8][2]
    #     cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

    #     cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
    #     cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
    #     cv2.line(img, (x1, y1), (x2, y2), (255,8,255), 3)
    #     cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
    
    #     length = math.hypot(x2 - x1, y2 - y1)

    #     vol = np.interp(length, [0, 200], [minVol, maxVol])
    #     print(int(length),vol)
    #     volume.SetMasterVolumeLevel(vol, None)

    #     if length < 50:
    #         cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
       
    if lmList:
        
        # Find how many fingers are up
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        cv2.putText(img,f'Fingers:{totalFingers}',(bbox[0] + 200, bbox[1] - 30),cv2.FONT_HERSHEY_PLAIN,2, (0, 255, 0), 2)
        
        # Perform operation based on fingers movement
        if totalFingers == 0:
            cv2.putText(img, " ",(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)

        elif totalFingers == 1:     
            p.press("volumeup")
            cv2.waitKey(1000)
            cv2.putText(img, "Volume UP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)

        elif totalFingers == 2:
            p.press("volumedown")
            cv2.waitKey(1000)    
            cv2.putText(img, "Volume Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        
        elif totalFingers == 3:
            p.press("left")
            cv2.waitKey(1000)            
            cv2.putText(img, "<<", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        
        elif totalFingers == 4:
            p.press("right")   
            cv2.waitKey(1000)     
            cv2.putText(img, ">>", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2)
        
        elif totalFingers == 5:
            p.press("space")   
            cv2.waitKey(1000)     
            cv2.putText(img, "Play/Pause", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2)

        else:
            pass
    
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)