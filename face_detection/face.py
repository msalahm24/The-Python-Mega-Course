import cv2
from PIL import Image, ImageDraw, ImageFilter
face_cascade=cv2.CascadeClassifier('13405_18147_bundle_archive/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('13405_18147_bundle_archive/haarcascade_eye.xml')
img=cv2.imread('mostafa.jpg')
cap=cv2.imread('tlbesa.jpg')
capre=cv2.resize(cap,(500,500))
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,
                                    scaleFactor=1.2,
                                    minNeighbors=5)
eyes = eye_cascade.detectMultiScale(gray_img,scaleFactor=1.2,minNeighbors=5)
for x,y,w,h in faces:
    postion=(int(x),(y))
    #cv2.rectangle(img,(x,y),(int(x+w/2),int(y+h/2)),(0,255,0),1)
    circle=cv2.circle(img,(int(x+w/2),int(y+h/2)),int(w/2),(0,255,0),1)
    crop_img = img[y:y+h, x:x+w]
crop_imgre=cv2.resize(crop_img,(118,100))
cv2.imwrite('new.jpg',crop_imgre)
img2=Image.open('new.jpg')
img1=Image.open('talbesa1.jpg')
img1.paste(img2,(219,83))
img1.save('result.jpg')
result=cv2.imread('result.jpg')
cv2.imshow('image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
