# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:42:01 2019

@author: Swapnil
"""

import cv2
import numpy as np

def fn():    
    for x in range(a):
        for y in range(b):
            if rando[x][y]==1.0 and img_gray[x][y]==255:
                img_gray[x][y]=0
            elif rando[x][y]==0.0 and img_gray[x][y]==255:
                img_gray[x][y]=255
            elif rando[x][y]==1.0 and img_gray[x][y]==0:
                img_gray[x][y]=255
            elif rando[x][y]==0.0 and img_gray[x][y]==0:
                img_gray[x][y]=0
    
    cv2.imshow('Gray',img_gray)
    cv2.waitKey(0)
    
def dualtone():
    for x in range(a):
        for y in range(b):
            if img_gray[x][y]<126:
                img_gray[x][y]=0
            else:
                img_gray[x][y]=255
        
def setrando():    
    for x in range(a):
        for y in range(b):
            if rando[x][y]<=0.5:
                rando[x][y]=int(0)
            else:
                rando[x][y]=int(1)

def setrandoimg():
        for x in range(a):
            for y in range(b):
                if rando[x][y]==1.0 and img_gray[x][y]==255:
                    img_gray[x][y]=0
                elif rando[x][y]==0.0 and img_gray[x][y]==255:
                    img_gray[x][y]=255
                elif rando[x][y]==1.0 and img_gray[x][y]==0:
                    img_gray[x][y]=255
                elif rando[x][y]==0.0 and img_gray[x][y]==0:
                    img_gray[x][y]=0
        cv2.imshow('Gray',img_gray)
        cv2.waitKey(0)
    

if __name__ == "__main__": 
    global img_gray
    img_gray= cv2.imread("D:\Programming\Python\Anaconda\input.png", cv2.IMREAD_GRAYSCALE)
    global a,b
    a,b=img_gray.shape
    global rando
    rando=np.random.random((a,b))
    setrando()
    dualtone()
    cv2.imshow('Gray',img_gray)
    cv2.waitKey(0)
    setrandoimg()
    fn()