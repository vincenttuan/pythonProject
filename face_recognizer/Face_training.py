# 匯入所需程式庫
import fnmatch
import os
import cv2
import numpy as np
from face_recognizer import Config


# 定義 walk_files 函式，
# 傳入參數:directory 指定尋訪目錄, match=’*’ 設定正則表示式做為搜尋比對用
def walk_files(directory, match='*'):
    # os.walk(directory)尋訪 directory 指定目錄下的所有檔案
    # 回傳值定義：
    # root:表 directory 指定目錄
    # dirs:表找到的檔案位於 directory 指定目錄下的哪個目錄中
    # files:表找到的檔案名(含 dirs)
    for root, dirs, files in os.walk(directory):
        # 尋找符合 match 條件的檔案
        for filename in fnmatch.filter(files, match):
            # 傳出完整路徑與檔名
            # yield 就像是 return 會傳回值，但又不中斷函式的執行
            yield os.path.join(root, filename)


# 定義 prepare_image 函式，傳入參數:filename:圖檔名
def prepare_image(filename):
    # 傳出灰階化、縮放後的圖片
    return Config.resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))


# 定義 normalize 函式，傳入參數:
# X:原始資料, low:正規化下限值, high:正規化上限值, dtype:指定資料型態
def normalize(X, low, high, dtype=None):
    # 將原始資料 X 轉換成陣列
    X = np.asarray(X)

    # 取出陣列中極大與極小值
    minX, maxX = np.min(X), np.max(X)

    # 扣除極小值，就像濾掉 offset 偏移值
    X = X - float(minX)

    # 除以全距，讓陣列中的元素變化落在 0..1 範圍
    X = X / float((maxX - minX))

    # 乘上指定全距
    X = X * (high-low)

    # 加上指定極小值，讓陣列中的元素變化落在 low..high 範圍
    X = X + low

    # 若未指定資料型態
    if dtype is None:
        # 則直接轉換成陣列
        return np.asarray(X)

    # 否則以資料型態轉換成陣列
    return np.asarray(X, dtype=dtype)


# 主程式
if __name__ == '__main__':
    print("讀取訓練影像集 ...")

    # 宣告人臉陣列變數 faces
    faces = []

    # 宣告正樣本陣列變數 labels
    labels = []

    # 正樣本數量計數器
    pos_count = 0

    # 負樣本數量計數器
    neg_count = 0
    # Read all positive images

    # 尋訪 config.POSITIVE_DIR 指定目錄中所有 *.pgm 檔案
    for filename in walk_files(Config.POSITIVE_DIR, '*.pgm'):
        # 將 filename 圖檔讀出，灰階化、縮放後的圖片，加入 faces 陣列中
        faces.append(prepare_image(filename))
        # 將 config.POSITIVE_LABEL 標籤，加入 labels 陣列中
        labels.append(Config.POSITIVE_LABEL)
        # 正樣本數量計數器增一
        pos_count += 1

    # 尋訪 config. NEGATIVE_DIR 指定目錄中所有 *.pgm 檔案
    for filename in walk_files(Config.NEGATIVE_DIR, '*.pgm'):
        # 將 filename 圖檔讀出，灰階化、縮放後的圖片，加入 faces 陣列中
        faces.append(prepare_image(filename))
        # 將 config.NEGATIVE_LABEL 標籤，加入 labels 陣列中
        labels.append(Config.NEGATIVE_LABEL)
        # 負樣本數量計數器增一
        neg_count += 1

    # 列印找到的正、負樣本數量訊息
    print('讀取:', pos_count, '正樣本影像, ', neg_count, '負樣本影像.')
    # Train model
    print('臉部模組訓練中...')

    # 建立特徵臉鑑別器
    model = cv2.face.EigenFaceRecognizer_create()

    # 進行機器學習
    model.train(np.asarray(faces), np.asarray(labels))

    # 將產出的訓練集儲存到 config.TRAINING_FILE 指定檔案
    model.write(Config.TRAINING_FILE)

    # 列印訓練集已儲存訊息
    print('訓練集資料已儲存在檔案路徑：', Config.TRAINING_FILE)

    # 取得均值樣本圖片
    mean = model.getMean().reshape(faces[0].shape)

    # 將均值樣本圖片正規化後儲存到 Config.MEAN_FILE 指定檔案
    cv2.imwrite(Config.MEAN_FILE, normalize(mean, 0, 255, dtype=np.uint8))

    # 取得特徵向量陣列
    eigenvectors = model.getEigenVectors()

    # 取得正樣本圖片
    pos_eigenvector = eigenvectors[:,0].reshape(faces[0].shape)

    # 將正樣本圖片正規化後儲存到 Config.POSITIVE_EIGENFACE_FILE 指定檔案
    cv2.imwrite(Config.POSITIVE_EIGENFACE_FILE, normalize(pos_eigenvector, 0, 255, dtype=np.uint8))

    # 取得負樣本圖片
    neg_eigenvector = eigenvectors[:,1].reshape(faces[0].shape)

    # 將負樣本圖片正規化後儲存到 Config.NEGATIVE_EIGENFACE_FILE 指定檔案
    cv2.imwrite(Config.NEGATIVE_EIGENFACE_FILE, normalize(neg_eigenvector, 0, 255, dtype=np.uint8))

