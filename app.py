import os
import cv2
from cvzone.HandTrackingModule import HandDetector #v1.4.1
import numpy as np
import time

#mediapipe v 08.8.0

vid = cv2.VideoCapture(0)
vid.set(3, 1920)
vid.set(4, 1080)
detector = HandDetector(detectionCon=0.8)
color = (0,0,255)
x = 0
cx,cy,w,h = 100,100,100,100
cxm,cym = 200,200
cxv,cyv = 300,300
cxs,cys = 400,400
while True:
    success,video = vid.read()
    video = cv2.flip(video,1)
    video = detector.findHands(video)
    lmList , _ = detector.findPosition(video)

    if lmList:

        l,_,_ =detector.findDistance(4,8,video)
        o,_,_ =detector.findDistance(8,12,video)
        print(l)
        if l < 35:
            cursor = lmList[8]
            if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
                cx,cy = cursor
            if cxm - w // 2 < cursor[0] < cxm + w // 2 and cym - h // 2 < cursor[1] < cym + h // 2:
                cxm,cym = cursor
            if cxv - w // 2 < cursor[0] < cxv + w // 2 and cyv - h // 2 < cursor[1] < cyv + h // 2:
                cxv,cyv = cursor
            if cxs - w // 2 < cursor[0] < cxs + w // 2 and cys - h // 2 < cursor[1] < cys + h // 2:
                cxs,cys = cursor
        if o < 35:
            cursor = lmList[8]
            if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
                time.sleep(1)
            if cxm - w // 2 < cursor[0] < cxm + w // 2 and cym - h // 2 < cursor[1] < cym + h // 2:
                os.startfile("C:\Program Files (x86)\Steam\steamapps\common\Celeste\Celeste.exe")
                time.sleep(1)
            if cxv - w // 2 < cursor[0] < cxv + w // 2 and cyv - h // 2 < cursor[1] < cyv + h // 2:
                os.startfile(r"C:\Users\eyupc\AppData\Local\Programs\Microsoft VS Code\Code.exe")
                time.sleep(1)
            if cxs - w // 2 < cursor[0] < cxs + w // 2 and cys - h // 2 < cursor[1] < cys + h // 2:
                os.startfile(r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe")
                time.sleep(1)

    videoNew = np.zeros_like(video,np.uint8)
    rect = cv2.rectangle(videoNew,(cx-w//2, cy-h//2),(cx+w//2, cy+h//2),color,cv2.FILLED)
    rect = cv2.putText(rect,'Chrome',(cx-30,cy),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),1)
    rect2 = cv2.rectangle(videoNew, ((cxm) - w // 2, (cym) - h // 2), ((cxm) + w // 2, (cym)+ h // 2), color, cv2.FILLED)
    rect2 = cv2.putText(rect2, 'Celeste', (cxm- 30, cym), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    rect3 = cv2.rectangle(videoNew, ((cxv) - w // 2, (cyv) - h // 2), ((cxv) + w // 2, (cyv) + h // 2), color,cv2.FILLED)
    rect3 = cv2.putText(rect3, 'Visual Code', (cxv - 30, cyv), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    rect4 = cv2.rectangle(videoNew, ((cxs) - w // 2, (cys) - h // 2), ((cxs) + w // 2, (cys) + h // 2), color,cv2.FILLED)
    rect4 = cv2.putText(rect4, 'Visual Studio', (cxs - 30, cys), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    out = video.copy()
    alpha = 0.5
    mask = videoNew.astype(bool)
    out[mask] = cv2.addWeighted(video,alpha,videoNew,1-alpha,0)[mask]
    cv2.imshow("Video",out)
    cv2.waitKey(1)