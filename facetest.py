import cv2
import numpy as np
import mysql.connector as sql
import os
mycon = sql.connect(host='localhost', user='root', passwd='root', database='test')
c = mycon.cursor()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
uname = input("Enter your name: ")
insertSQL = """INSERT INTO users (name)VALUES(%s)"""
c.execute(insertSQL, (uname,))

uid = c.lastrowid
sampleNum = 0
while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    sampleNum = sampleNum+1
    cv2.imwrite("dataset/Betterphone."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.waitKey(100)
  cv2.imshow('img',img)
  cv2.waitKey(1);
  if sampleNum > 20:
    break
cap.release()
mycon.commit()
mycon.close()
cv2.destroyAllWindows()