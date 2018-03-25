# -*- coding: utf-8 -*-
import requests
import re

#urls = 'https://movie.douban.com/top250?start=&filter='
i = '豆瓣评分:'.decode('utf-8')

def get_html(urls):
    html = requests.get(urls)
    return html.text

def get_move(html):
    pattern = re.compile(r'<ol class="grid_view">.*?</ol>',re.S)
    move = pattern.findall(html)
    htmls = move[0]
    return htmls

def get_date(htmls):
    pattern = re.compile(r'<em class="">(\d{1,3})</em>.*?<div class="hd">.*?<a href="https://movie.douban.com/subject/(\d{1,8})/".*?<span class="title">(.*?)</span>.*?<div class="star">.*?<span class="rating_num" property="v:average">(.*?)</span>',re.S)#排名/地址/片名/评分
    date = pattern.findall(htmls)
    return date

def print_date(dates, f):
    for date in dates:
         s = 'NO.'+str(date[0]) + '\n\t'+date[2]+'\t' + i +'  ' + str(date[3]) + '\n'*2 + 'https://movie.douban.com/subject/' + str(date[1]) + '/' + '\n'*2
         f.write(s.encode('utf-8'))

def main():
    f = open('/home/chushi/douban1.txt','w')
    for n in range(0,251,25):
        urls = 'https://movie.douban.com/top250?start='+str(n)+'&filter='
        html = get_html(urls)
        htmls = get_move(html)
        dates = get_date(htmls)
        print_date(dates, f)
    f.close()

if __name__ == '__main__':
    main()
