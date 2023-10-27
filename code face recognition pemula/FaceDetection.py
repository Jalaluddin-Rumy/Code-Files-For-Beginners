
import cv2, os
import numpy

cam = cv2.VideoCapture(1)
cam.set(3, 640) #ubah lebar cam
cam.set(4, 480) #ubah tinggi cam

#deteksi wajah menggunakan file haarcascade_frontalface_default.xml
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    retV, frame = cam.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDetector.detectMultiScale(gray, 1.3, 5) #frame, scaleFactor, minNeighbors 
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)

    cv2.imshow("Kamera Nyala", frame)
    cv2.imshow("Kamera gray Nyala", gray)
    k = cv2.waitKey(1) & 0xff
    if k == 27 or k == ord("x"):
    #if cv2.waitKey(1) & 0xff == ord("x"):
        break

cam.release()
cv2.destroyAllWindows()