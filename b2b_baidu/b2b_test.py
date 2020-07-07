import urllib.request
import os
import re
import time
import random


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html


def get_page(url):  # 获取第一页中所有超链接
    html = url_open(url).decode('gb2312', 'ignore')
    addrs = []

    addrs = re.findall(r"http://www.meizitu.com/a/\d\d\d\d\.html", html)

    # print('get_page被调用', addrs)
    # print('共有%d个元素' % len(addrs))
    return addrs


def get_img_url(urllist):  # 获取每一超链接中所有图片地址
    img_url = []
    for each in urllist:
        html = url_open(each).decode('gb2312', 'ignore')
        temp = re.findall('http://mm.chinasareview.com/wp-content/uploads/2017a/08/\d\d/\d\d\.jpg', html)
        for i in temp:
            img_url.append(i)

    print('调用get_img_url')
    print('get_img_url获取的地址有：', img_url)
    return img_url


def save(img_url):
    for each in img_url:
        print('each is ', each)
        filename = "".join('%s' % i for i in (each.split('/')[5:9]))
        print('文件名是：', filename)
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download(folder='mm', pages=10):
    url = 'http://www.meizitu.com/a/more_1.html'
    os.mkdir(folder)
    os.chdir(folder)
    urllist = get_page(url)  # 获取第一页中所有超链接
    img_url = get_img_url(urllist)  # 获取每个超链接中所有图片地址
    save(img_url)


if __name__ == '__main__':
    download()
