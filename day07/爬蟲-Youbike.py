# 網路位置: https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
import json
import requests

if __name__ == '__main__':
    url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    youbikes = json.loads(requests.get(url).text)
    print(len(youbikes))
    # sna 站台, tot 總量, sbi 可借數量, bemp 可還數量, ar 地址

    addr = '忠孝東路四段'
    for item in youbikes:
        if addr in item['ar']:
            print('可借:{} 可還:{} {} {}'.format(item['sbi'], item['bemp'], item['ar'], item['sna']))


