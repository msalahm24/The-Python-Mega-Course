import cv2

img=cv2.imread('3.1 galaxy.jpg.jpg',0)
imgre=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow('im',imgre)
cv2.imwrite('new_re.jpg',imgre)
cv2.waitKey(0)
cv2.destroyAllWindows()

