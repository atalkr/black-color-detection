# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 13:57:46 2019

@author: atalk
"""
import imutils
import numpy as np
import cv2

cap=cv2.VideoCapture(0)
threshold_value=9000000
while True:
    res,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([0,0,0])
    high=np.array([128,128,128])
    
    mask=cv2.inRange(hsv,lower,high)
    value =np.sum(mask)
    if(value>threshold_value):
        # hardware activation code
        print("activate the robotic arm")
    else:
        print("system idle")
    kernel=np.ones((15,15),np.float32)/255
    smoothed=cv2.filter2D(mask,-1,kernel)
    
    blur=cv2.GaussianBlur(mask,(15,15),0)
    median=cv2.medianBlur(mask,5)
    bilateral=cv2.bilateralFilter(mask,15,75,75)
    cv2.imshow('smoothed frame',smoothed)
    cv2.imshow('blurred frame',blur)
    cv2.imshow('median frame',median)
    cv2.imshow('bilateral frame',bilateral)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()