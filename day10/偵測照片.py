# 偵測照片, 並將人臉, 眼睛, 微笑偵測出來
# 安裝: pillow, opencv-python, opencv-contrib-python
import cv2
# 人臉特徵檔
face_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")
print(face_cascade)

# 讀取影像(原始圖)
frame = cv2.imread("./sample_image/test.jpg")

# 讀取灰階影像
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 顯示影像
cv2.imshow('My image', gray)

# 按下任意鍵離開
c = cv2.waitKey(0)
print(c)


