import cv2
import keyboard

color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0),"white":(255,255,255)}


def detect_nose(img, faceCascade):
    #convert image to gray scale
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #features is detected in gray-scale image which returns coordinates,width and height of features
    features = faceCascade.detectMultiScale(gray_img,1.1,8)
    nose_cords = []

    #drawing rectangle around feature
    for(x,y,w,h) in features:
        cv2.circle(img,(((2*x+w)//2),(2*y+h)//2),10,color['green'],2)
        #to see face-boundary too
        #cv2.rectangle(img,(x,y),(x+w,y+h),color['green'],2)
        nose_cords = ((2*x+w)//2,(2*y+h)//2)

    return img, nose_cords

