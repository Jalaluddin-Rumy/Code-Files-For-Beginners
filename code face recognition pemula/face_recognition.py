import cv2

cascade_wajah = cv2.CascadeClassifier("haarcascade_face.xml")

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade_wajah.detectMultiScale(gray, 1.3, 3)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Deteksi wajah", frame)

    if cv2.waitKey(1) & 0xff == ord('x'):
        break

cam.release()
cv2.destroyAllWindows()