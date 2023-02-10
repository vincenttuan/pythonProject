# 發送位置: https://notify-api.line.me/api/notify
# token = ody4CpIUb1Su3Wof2sUdxaWrVF7zzqLc5XApBqg36Od
import requests

if __name__ == '__main__':
    url = 'https://notify-api.line.me/api/notify'
    token = 'ody4CpIUb1Su3Wof2sUdxaWrVF7zzqLc5XApBqg36Od'
    headers = {
        "Authorization": "Bearer " + token
    }
    # 輸入要傳送的資料
    message = input('請輸入文字訊息(1000字內):')
    params = {
        "message": message
    }
    # 傳送到 LineNotify
    resp = requests.post(url, headers=headers, params=params)
    print(resp)  # 若看到 200 表示成功


