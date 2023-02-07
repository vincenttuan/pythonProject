# 資料來源: https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx
import json
import requests

if __name__ == '__main__':
    # 1. 取得原始資料
    url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
    source = requests.get(url).text
    print(type(source))
    print(source)


