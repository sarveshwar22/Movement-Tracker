import cv2
import keyboard

color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0),"white":(255,255,255)}


def detect_nose(img, faceCascade):
    #convert image to gray scale
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #features is detected in gray-scale image which returns coordinates,width and height of features
    