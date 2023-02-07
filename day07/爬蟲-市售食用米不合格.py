# 資料來源: https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx
import json
import requests

if __name__ == '__main__':
    # 1. 取得原始資料
    url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
    source = requests.get(url).text
    # print(type(source))
    # print(source)
    # 2. 將 json str 轉為 數組 以利後續分析
    data = json.loads(source)  # data 就是可分析的數組(list)
    print('資料型態:', type(data))
    print('資料筆數:', len(data))
    print('資料內容:', data)
    # 3. 決定要使用的資料欄位有哪些(option) ?
    # 品名, 廠商名稱, 不合格原因, 行政處分
    bad_rice = []
    for item in data:
        rice = {}
        rice.setdefault('品名', item['品名'])
        rice.setdefault('廠商名稱', item['廠商名稱'])
        rice.setdefault('不合格原因', item['不合格原因'])
        rice.setdefault('行政處分', item['行政處分'])
        bad_rice.append(rice)
    print('bad_rice:')
    print(bad_rice)
    # 4. 分析
    keyword = input('請輸入品名關鍵字: ')
    result = []  # 存放分析的結果
    for item in bad_rice:
        if keyword in item['品名']:
            result.append(item)  # 將符合的資料放入 result 中
    # 5 印出分析結果
    print('分析結果')
    for item in result:
        print(item)





