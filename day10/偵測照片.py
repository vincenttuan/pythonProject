# 偵測照片, 並將人臉, 眼睛, 微笑偵測出來
# 安裝: pillow, opencv-python, opencv-contrib-python
import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")
# print(face_cascade)

# 讀取影像(原始圖)
frame = cv2.imread("./sample_image/test.jpg")

# 讀取灰階影像
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 偵測臉部
faces = face_cascade.detectMultiScale(
    gray,  # 待偵測的圖像
    scaleFactor=1.1,  # 檢測粒度(越小越精準(但是速度辨識會慢))
    minNeighbors=10,  # 區塊檢測次數(目標區塊只少要通過幾次檢測才算成功)
    minSize=(30, 30), # 區塊大小
    flags=cv2.CASCADE_SCALE_IMAGE  # 比對類型
)
print('臉部座標:', faces)


# 顯示影像
cv2.imshow('My image', frame)

# 按下任意鍵離開
c = cv2.waitKey(0)
print(c)


