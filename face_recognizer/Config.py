import cv2

# 訓練對象人名(請輸入自己的名字) ?
MY_NAME = 'vincent'

# 樣本素材張數
SAMPLE_AMOUNT = 200

# 定義均值圖檔檔名
MEAN_FILE = './training/mean.png'

# 定義正片圖檔檔名
POSITIVE_EIGENFACE_FILE = './training/positive_eigenface.png'

# 定義負片圖檔檔名
NEGATIVE_EIGENFACE_FILE = './training/negative_eigenface.png'

# 定義正樣本檔案檔名的前置詞為 positive_
POSITIVE_FILE_PREFIX = 'positive_'

# 辨識特徵數
COMPONENT_NUMBER = 80

# 辨識信心水準
POSITIVE_THRESHOLD = 2000.0

# 特定人臉辨識訓練集檔名
TRAINING_FILE = './training/' + MY_NAME + '_training.haarcascades'

# 正樣本目錄名
POSITIVE_DIR = './training/positive'

# 負樣本目錄名
NEGATIVE_DIR = './training/negative'

# 辨識結果允收的狀態旗標
POSITIVE_LABEL = 1

# 辨識結果拒絕的狀態旗標
NEGATIVE_LABEL = 2

# 人臉辨識訓練集
HAAR_FACES = './xml/haarcascade_frontalface_alt.xml'

# 取樣縮放比例
HAAR_SCALE_FACTOR = 1.1

# 取樣最小寬放數
HAAR_MIN_NEIGHBORS = 10

# 取樣最小樣本尺寸
HAAR_MIN_SIZE = (30, 30)

# 辨識相片寬的像素數
FACE_WIDTH = 92

# 辨識相片高的像素數量
FACE_HEIGHT = 112


# 定義 detect_single 函式，傳入 image 與 haar_faces
def detect_single(image, haar_faces):
    # 層疊分類器進行多物件檢測
    faces = haar_faces.detectMultiScale(image,
        scaleFactor = HAAR_SCALE_FACTOR,
        minNeighbors = HAAR_MIN_NEIGHBORS,
        minSize = HAAR_MIN_SIZE,
        flags = cv2.CASCADE_SCALE_IMAGE)

    # 若找不到人臉或不只一張人臉
    if len(faces) != 1:
        # 則傳出 無
        return None

    # 否則傳出陣列中第 0 個人臉物件
    return faces[0]


# 定義 crop 函式
# 裁剪框由 x，y（左上角）和 w，h（寬度和高度）定義到與 face_recognizer 訓練數據具有相同寬高比的圖像。
# 如果框位於圖像邊緣附近，則返回較小的裁剪。
def crop(image, x, y, w, h):
    # 以樣本的高寬比來計算出所需的高度
    crop_height = int((FACE_HEIGHT / float(FACE_WIDTH)) * w)

    # 取得裁切區域中心座標之縱座標
    midy = y + h/2

    # 計算出來源圖片範圍內的裁切區域上方縱座標
    y1 = int(max(0, midy-crop_height/2))

    # 計算出來源圖片範圍內的裁切區域下方縱座標
    y2 = int(min(image.shape[0]-1, midy+crop_height/2))

    # 傳出來源圖片的裁切區域(x, y1)~(x+w, y2)圖片
    return image[y1:y2, x:x+w]


# 定義 resize 函式
def resize(image):
    # 傳出 image 縮放為 FACE_WIDTH, FACE_HEIGHT 的圖片
    # 插值演算法：INTER_LANCZOS4 = 8x8像素領域的 Lanczos 插值
    return cv2.resize(image, (FACE_WIDTH, FACE_HEIGHT), interpolation=cv2.INTER_LANCZOS4)
