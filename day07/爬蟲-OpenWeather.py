# 網路位置: https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}
if __name__ == '__main__':
    city_name = 'taipei'
    key = '1b5307db9ae068d9b14059506ded8b0e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}'.format(city_name, key)
    print(url)

