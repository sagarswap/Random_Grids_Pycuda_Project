import cv2
import threading
import numpy as np

def fn(m):    
    for x in range(m, a, 4):
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

def setrandoimg(m):
        for x in range(m, a, 4):
            for y in range(b):
                if rando[x][y]==1.0 and img_gray[x][y]==255:
                    img_gray[x][y]=0
                elif rando[x][y]==0.0 and img_gray[x][y]==255:
                    img_gray[x][y]=255
                elif rando[x][y]==1.0 and img_gray[x][y]==0:
                    img_gray[x][y]=255
                elif rando[x][y]==0.0 and img_gray[x][y]==0:
                    img_gray[x][y]=0
    
def dualtone(m):
    for x in range(m, a, 4):
        for y in range(b):
            if img_gray[x][y]<126:
                img_gray[x][y]=0
            else:
                img_gray[x][y]=255
        
def setrando(m):    
    for x in range(m, a, 4):
        for y in range(b):
            if rando[x][y]<=0.5:
                rando[x][y]=int(0)
            else:
                rando[x][y]=int(1)
                
def createargs():
    tname=threading.current_thread().name
    if tname=='t1':
        dualtone(0)
        setrando(0)
    elif tname=='t2':
        dualtone(1)
        setrando(1)
    elif tname=='t3':
        dualtone(2)
        setrando(2)
    elif tname=='t4':
        dualtone(3)
        setrando(3)
    tname.join()
    cv2.imshow('Gray',img_gray)
    cv2.waitKey(0)
    print(rando)
        
    
def threader():
    global rando
    rando=np.random.random((a,b))
    t1 = threading.Thread(target=createargs, name='t1')
    t2 = threading.Thread(target=createargs, name='t2') 
    t3 = threading.Thread(target=createargs, name='t3') 
    t4 = threading.Thread(target=createargs, name='t4') 
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t1 = threading.Thread(target=fn, name='t1')
    t2 = threading.Thread(target=fn, name='t2') 
    t3 = threading.Thread(target=fn, name='t3') 
    t4 = threading.Thread(target=fn, name='t4') 
    t1.start(0)
    t2.start(1)
    t3.start(2)
    t4.start(3)
    t1.join(0)
    t2.join(1)
    t3.join(2)
    t4.join(3)
    cv2.imshow('Gray',img_gray)
    cv2.waitKey(0)
    t1 = threading.Thread(target=setrandoimg, name='t1')
    t2 = threading.Thread(target=setrandoimg, name='t2') 
    t3 = threading.Thread(target=setrandoimg, name='t3') 
    t4 = threading.Thread(target=setrandoimg, name='t4') 
    t1.start(0)
    t2.start(1)
    t3.start(2)
    t4.start(3)
    t1.join(0)
    t2.join(1)
    t3.join(2)
    t4.join(3)

if __name__ == "__main__": 
    global img_gray
    img_gray= cv2.imread("D:\Programming\Python\Anaconda\input.png", cv2.IMREAD_GRAYSCALE)
    global a,b
    a,b=img_gray.shape
    threader()