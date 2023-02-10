import cv2

cap = cv2.VideoCapture(0)
print(cap)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # 320, 640, 800, 1024
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # 240, 480, 600, 768

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')
print(face_cascade)
while True:
    ret, frame = cap.read()  # 捕捉影像資料
    print(ret, frame)
    if ret == True:
        # 偵測人臉
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 偵測臉部，得到臉部區域座標與長寬(x, y, w, h)
        faces = face_cascade.detectMultiScale(
            gray,  # 待檢測圖片
            scaleFactor=1.1,  # 檢測粒度(數字越小越精準(速度慢), 反之數字越大越模糊(速度快))
            minNeighbors=15,  # 檢測次數(每個目標至少要檢測通過幾次才算成功，才被認定是 face)
            minSize=(30, 30),  # 搜尋比對最小尺寸
            flags=cv2.CASCADE_SCALE_IMAGE  # 比對物類型
        )
        # 在 face 周圍畫上矩形
        for (x, y, w, h) in faces:
            # 參數：frame, 坐上角座標, 右下角座標, BGR 色碼, 框線的寬度
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 顯示影像
    cv2.imshow('My Window', frame)
    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 將視窗全部清除
cap.release()
cv2.destroyAllWindows()