from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.request

import time

#webdriver 설정
browser = webdriver.Chrome('./webdriver/chromedriver')

#크롬 브라우저 내부 대기
browser.implicitly_wait(5)

#브라우저 사이즈
browser.set_window_size(1920, 1280)

#페이지 이동
browser.get("https://unsplash.com/t/nature")

#현재 페이지
cur_page = 1
#최대 페이지
max_page = 6

#while(cur_page <= max_page):
#bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

#이미지 그리드 가져오기
img_list = soup.select('div.VQW0y.Jl9NH > img')
for i in range(len(img_list)):
    imgUrl = img_list[i].get('src')
    urllib.request.urlretrieve(imgUrl, "./img/" + "test_" + str(i) + ".jpg")
