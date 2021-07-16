import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req # 파일을 다운로드 하기 위한 모듈
from bs4 import BeautifulSoup # 내용을 파싱하기 위한 모듈
import os.path

# 다운로드 URL
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = 'D:\Django\\workspace\\WebCrawling\\C3_DataProcessing\\forecast.xml'

# 데이터를 얻기 위해 매번 접근한다면 사이트에 부하가 갈 수 있기 때문에 한번 접근할 때 정보를 미리 다 받아온다.
if not os.path.exists(savename) : # 파일이 존재하지 않는다면
    req.urlretrieve(url, savename)

# BeautifulSoup 파싱
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup()
