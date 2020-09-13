#coding=utf-8
import re
import os
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
}

base_page_url = 'https://www.tujigu.com/a/5598/'
page_url_list = []
for i in range(2, 15):
    url =base_page_url+str(i)+'.html'
    page_url_list.append(url)
print(page_url_list)


def download_img(img_url, dir_name):
    img_name = img_url.split('/')[-1]
    img_response = requests.get(img_url)

    with open("d:/Download/"+dir_name+'/'+img_name, 'wb') as f:
        f.write(img_response.content)


def get_page(page_url):
    response = requests.get(page_url)
    response.encoding='utf-8'
    html = response.text

    img_urls = re.findall('<img src="(.*?)" alt=".*?" class="tupian_img">', html)
    print(img_urls)
    dir_name = re.findall('<img src=".*?" alt="(.*?)" class="tupian_img">', html)[0][16:29]
    print(dir_name)

    if not os.path.exists("d:/Download/"+dir_name):
        os.mkdir("d:/Download/"+dir_name)

    for img_url in img_urls:
        time.sleep(1)
        download_img(img_url, dir_name)

def main():
    for page_url in page_url_list:
        get_page(page_url)

if __name__ == "__main__":
    main()