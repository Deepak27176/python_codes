import cv2
import numpy as np

# reading image ![](img.png)
img = cv2.imread("mypic.jpeg")

# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 206, cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 13, 14)

# Cartoonization
color = cv2.bilateralFilter(img, 150, 255, 255)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
