import cv2
img=cv2.imread("linkedin.jpeg")
greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("greayimage.png",greyimg)
cv2.waitKey(0)
cv2.destroyAllWindows()