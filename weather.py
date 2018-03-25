import requests
from bs4 import BeautifulSoup
import lxml
import re

def getHtml(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    return html.text

def getDate(html):
    soup = BeautifulSoup(html, 'lxml')
    date = soup.find_all('script')
    '''
    for tag in date:
        print(tag.get_text())
    '''
    weather = date[2]
    return weather

def getWeather(date):
    pattern = re.compile(r'var\shour\ddata=.*?:.*?"(.*?)"],')
    weather = pattern.search(str(date))
    print(weather.group())

def main():
    url = 'http://www.weather.com.cn/weather1d/101190401.shtml'
    html = getHtml(url)
    date = getDate(html)
    getWeather(date)

if __name__ == '__main__':
    main()
