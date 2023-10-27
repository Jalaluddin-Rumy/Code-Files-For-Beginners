
import cv2

cam = cv2.VideoCapture(0)

while True:
    retV, frame = cam.read()
    #frame = cv2.flip(frame, 1)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("Kamera gray Nyala", gray)
    cv2.imshow("Kamera Nyala", frame)
    k = cv2.waitKey(1) & 0xff
    #if k == 27 or k == ord("x"):
    if cv2.waitKey(1) & 0xff == ord("x"):
        break

cam.release()
cv2.destroyAllWindows()