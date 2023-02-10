# 偵測照片, 並將人臉, 眼睛, 微笑偵測出來
# 安裝: pillow, opencv-python, opencv-contrib-python
import cv2
# 人臉特徵檔
face_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")
print(face_cascade)