#program threshold sederhana

#mengambil opencv & numpy
import cv2
import numpy as np

#membaca gambar
gambar = cv2.imread ('lena.jpg')

#convert gambar rgb jadi grayscale
grayscale = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

#beri threshold gausian dan binary
threshold = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#coba dgn threshold lain
retval, cobalain = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#menampilkan gmbr asli
cv2.imshow('Gambar Asli', gambar)
#menampilkan gmbr hasil threshold
cv2.imshow('Hasil Gausian', threshold)
cv2.imshow('Hasil Otsu', cobalain)

#penutup program bila ditekan sembarang tombol
cv2.waitKey(0)
#menghapus memori
cv2.destroyAllWindows()

