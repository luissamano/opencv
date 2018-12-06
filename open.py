import cv2
 
# Cargamos la imagen del disco duro
imagen = cv2.imread("images\img.jpg")
 
cv2.imshow("prueba", imagen)
cv2.waitKey(0)