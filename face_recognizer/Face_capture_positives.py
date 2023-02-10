# 匯入所需程式庫
import glob
import os
import cv2
from face_recognizer import Config


# 載入 Config.HAAR_FACES 指定的層疊分類器
haar_faces = cv2.CascadeClassifier(Config.HAAR_FACES)

# 主程式
if __name__ == '__main__':
    # 取得攝像鏡頭位置
    camera = cv2.VideoCapture(0)

    # 設定攝像鏡頭捕捉區域
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 假如 config.POSITIVE_DIR 指定的目錄不存在
    if not os.path.exists(Config.POSITIVE_DIR):
        # 新增 config.POSITIVE_DIR 指定的目錄
        os.makedirs(Config.POSITIVE_DIR)

    # 找出 config.POSITIVE_DIR 指定的目錄符合檔案名規則的檔案
    files = sorted(glob.glob(os.path.join(Config.POSITIVE_DIR,
                                          Config.POSITIVE_FILE_PREFIX + '[0-9][0-9][0-9].pgm')))
    # 設定計算器為 0
    count = 0

    # 若找到既有的正樣本檔案
    if len(files) > 0:
        # 計算出下個檔案編號
        count = int(files[-1][-7:-4]) + 1

    print('捕獲到正確的訓練圖像')

    # 無窮迴圈
    while True:
        # 捕捉 frame-by-frame (讀取相片)
        ret, image = camera.read()  # ret : 讀到的 frame 是正確的話會回傳 true

        # 利用 OpenCV 轉為灰階相片
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # 進行判斷是否是單一人臉的相片
        result = Config.detect_single(gray, haar_faces)

        # 若不是單一人臉的相片
        if result is None:
            # 列印錯誤並請重拍的訊息
            print('無法檢測到單個 face_recognizer (只可以有一個臉，其他人請讓開)！檢查capture.pgm中的圖像以查看捕獲的內容，並再次嘗試。')
            # 回到迴圈起始位置(重拍)
            continue

        # 取得欲裁切的資料
        x, y, w, h = result

        # 繪製人臉框與名字
        cv2.putText(image, Config.MY_NAME, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 255, 0), 2)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 5)

        # 將 frame 顯示於視窗中 (這樣才可以看到自己的臉)
        cv2.imshow('Video', image)

        # 進行裁切
        crop = Config.crop(gray, x, y, w, h)

        # 產生新編檔名
        filename = os.path.join(Config.POSITIVE_DIR, Config.POSITIVE_FILE_PREFIX + '%03d.pgm' % count)

        # 將裁切、縮放、灰階化後得圖片依新編檔名寫入 config.POSITIVE_DIR 指定的目錄
        cv2.imwrite(filename, crop)

        # 列印成功儲存訊息
        print('找到 face_recognizer 並儲存培訓圖片', filename)

        # 編號加 1
        count += 1

        # count > SAMPLE_AMOUNT 離開
        if count > Config.SAMPLE_AMOUNT:
            print("Finish")
            break;

        # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放資源
    camera.release()

    # 關閉所有視窗
    cv2.destroyAllWindows()
