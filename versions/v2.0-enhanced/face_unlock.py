import cv2, os, numpy as np, pyautogui

recognizer = cv2.face.LBPHFaceRecognizer_create()
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def try_face_unlock():
    recognizer.read("trainer.yml")   # you must train once first
    cam = cv2.VideoCapture(0)
    for _ in range(30):
        ok, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi)
            if conf < 70:
                print("Face recognized – unlocking!")
                pyautogui.press("enter")  # simulate unlock
                cam.release()
                return
    cam.release()
    print("Face not recognized.")