# 資料來源: 台灣證券交易所
# 資料位置: https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={}&selectType=ALL
# 資料格式: 證券代號 證券名稱 殖利率(%) 股利年度 本益比 股價淨值比 財報年/季
import requests
import datetime as dt

if __name__ == '__main__':
    date = dt.datetime(2023, 2, 7)  # 得到日期物件
    print(date, type(date))
    date_str = date.strftime('%Y%m%d')
    print(date_str, type(date_str))
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={}&selectType=ALL'.format(date_str)
    data = requests.get(url).text
    # print(data)
    stocks = []
    for row in data.split("\r\n"):
        stock = row.split('","')
        if len(stock) == 7:
            # print(stock)
            try:
                dict = {}
                dict.setdefault('證券代號', stock[0].replace('"', ''))
                dict.setdefault('證券名稱', stock[1])
                dict.setdefault('殖利率', float(stock[2]))
                dict.setdefault('股利年度', stock[3])
                dict.setdefault('本益比', float(stock[4]))
                dict.setdefault('股價淨值比', float(stock[5]))
                dict.setdefault('財報', stock[6].replace('",', ''))
                # print(dict)
                stocks.append(dict)
            except ValueError:
                pass

    print(len(stocks))
    print(stocks)
