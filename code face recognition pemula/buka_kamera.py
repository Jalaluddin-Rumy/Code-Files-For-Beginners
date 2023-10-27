
import cv2

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("Kamera gray Nyala", gray)
    cv2.imshow("Kamera Nyala", img)
    if cv2.waitKey(27) & 0xff == ord("x"):
        break

cam.release()
cv2.destroyAllWindows()
