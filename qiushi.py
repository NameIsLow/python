#-*- encoding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        html = requests.get(url, headers=headers)
        '''
        print html.status_code
        print html.raise_for_status()
        print html.text
        '''
        return html.text
    except:
        print 'ss'

def getDate(html):
    soup = BeautifulSoup(html, 'html.parser')
    dates = soup.find_all('div', 'content')
    pattern = re.compile(r'<span>(.*?)</span>',re.S)
    for date in dates:
        text = re.search(pattern, str(date))
        print text.group(1).replace('<br/>', '  ')
        raw_input('回车翻页:')
def main():
    
    for i in range(0,13):
        url = 'https://www.qiushibaike.com/text/page/'+str(i)
        html = getHtml(url)
        getDate(html)

if __name__ == '__main__':
    main()
            
    
