# 網路位置: https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}
import json
import requests
if __name__ == '__main__':
    city_name = 'taipei'
    key = '1b5307db9ae068d9b14059506ded8b0e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}'.format(city_name, key)
    print(url)
    data = json.loads(requests.get(url).text)
    print(data)
    weather_main = data['weather'][0]['main']
    weather_description = data['weather'][0]['description']
    weather_temp = '{:.2f}°C'.format(data['main']['temp'] - 273.15)
    weather_feels_like = '{:.2f}°C'.format(data['main']['feels_like'] - 273.15)
    weather_humidity = '{}%'.format(data['main']['humidity'])
    weather_clouds = '{}%'.format(data['clouds']['all'])
    weather_wind_speed = '{} m/s'.format(data['wind']['speed'])
    # 建立 weather 字典數組
    weather = {}
    weather.setdefault('天氣狀態', weather_main)
    weather.setdefault('天氣敘述', weather_description)
    weather.setdefault('現在溫度', weather_temp)
    weather.setdefault('體感溫度', weather_feels_like)
    weather.setdefault('現在濕度', weather_humidity)
    weather.setdefault('雲層覆蓋', weather_clouds)
    weather.setdefault('每秒風速', weather_wind_speed)
    print(weather)
    # 根據 key 值逐一將字典資料印出
    for key in weather.keys():
        print(key, weather[key])


