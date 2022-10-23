import cv2
img = cv2.imread("~/Desktop/Image.png")
faceCascade = cv2.CascadeClassifier("./Desktop/haarcascade_frontalface_default.xml")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
while True:
    cv2.imshow("Image",img)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break