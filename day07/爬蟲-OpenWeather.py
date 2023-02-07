# 網路位置: https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}
if __name__ == '__main__':
    city_name = 'taipei'
    key = 'your key'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}'.format(city_name, key)
    print(url)

