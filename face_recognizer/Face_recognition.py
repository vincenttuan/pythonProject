# 匯入所需程式庫
import cv2
from face_recognizer import Config

# 載入 Config.HAAR_FACES 指定的層疊分類器
haar_faces = cv2.CascadeClassifier(Config.HAAR_FACES)

if __name__ == '__main__':


    # 取得攝像鏡頭位置
    cap = cv2.VideoCapture(0)

    # 設定攝像鏡頭捕捉區域
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 列印訓練集資料載入中訊息
    print('訓練集資料載入中 ...')

    # 依 Config.COMPONENT_NUMBER 指定的特徵數量、Config.POSITIVE_THRESHOLD 允收距離，來建立特徵臉鑑別器
    model = cv2.face.EigenFaceRecognizer_create(Config.COMPONENT_NUMBER, Config.POSITIVE_THRESHOLD)

    # 載入 Config.TRAINING_FILE 指定的訓練集檔案
    model.read(Config.TRAINING_FILE)

    # 列印訓練集資料完成載入訊息
    print('訓練集資料載入完成 !')

    # 開始循環偵測
    while True:

        # 捕捉 frame-by-frame
        ret, frame = cap.read()  # ret : 讀到的 frame 是正確的話會回傳 true

        # 將圖片灰階化
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 開始辨識程序...begin

        # 1.判斷是否為單一人臉的圖片
        result = Config.detect_single(gray, haar_faces)

        # 2.判斷 result 有無回傳值
        if result is None:
            print('無法偵測到單一人臉 face_recognizer !')
            # 將 frame 顯示
            cv2.imshow('Recognition', frame)
            # 重新偵測
            continue

        # 3.取得欲裁切的資料
        x, y, w, h = result

        # 4.進行裁切放人臉圖片
        crop = Config.resize(Config.crop(gray, x, y, w, h))

        # 5.進行比對檢驗評估
        label = model.predict(crop)

        # 6.列印評估資訊
        print(label)

        # 畫出每一個臉的範圍
        faces = haar_faces.detectMultiScale(
            gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
            scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
            # 表示在前後兩次相繼的掃描中，搜尋視窗的比例係數。預設為1.1，即每次搜尋視窗依次擴大10%
            minNeighbors=5,  # 每個目標至少檢測到幾次以上，才可被認定是真數據。
            minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)，也就是太小的臉就忽略辨識
            flags=cv2.CASCADE_SCALE_IMAGE
            # CASCADE_DO_CANNY_PRUNING=1 -> 利用canny邊緣檢測來排除一些邊緣很少或者很多的影象區域
            # CASCADE_SCALE_IMAGE=2 -> 正常比例檢測
            # CASCADE_FIND_BIGGEST_OBJECT=4 -> 只檢測最大的物體
            # CASCADE_DO_ROUGH_SEARCH=8 粗略的檢測
        )

        # 印出 label[1] 辨識分數
        cv2.putText(frame, str(int(label[1])), (10, 30), 2, 1.2, (255, 0, 0), 2)

        # 7.判斷評估值 <= Config.POSITIVE_THRESHOLD
        if label[1] <= Config.POSITIVE_THRESHOLD:
            # 印出辨識成功
            print('辨識成功 face_recognizer!')
            # 開門
            # gl.set_value('door', '1')
            # 在臉部周圍畫矩形框
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)  # 注意：(0, 255, 0) 是 BGR
                # 繪文字
                cv2.putText(frame, Config.MY_NAME, (x, y - 7), 2, 1.2, (0, 255, 0), 2)

            # 跳出循環偵測回圈
            # break
        else:
            # 印出辨識失敗
            print('辨識失敗 face_recognizer!')
            # 在臉部周圍畫矩形框
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)  # 注意：(0, 255, 0) 是 BGR

        # 結束辨識程序...end

        # 將 frame 顯示
        cv2.imshow('Recognition', frame)

    # 釋放資源
    cap.release()

    # 關閉所有視窗
    cv2.destroyAllWindows()
