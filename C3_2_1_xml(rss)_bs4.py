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
if not os.path.exists(savename): # 파일이 존재하지 않는다면
    req.urlretrieve(url, savename)

# BeautifulSoup 파싱
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

# 지역 확인
info = { } # Key값은 도시의 이름, Value값은 파이썬 배열의 형태로 각 시간별 최저온도
for location in soup.find_all("location"):
    loc = location.find("city").string
    # print(loc)
    weather = location.find_all("tmn")
    # print(weather)
    if not (loc in info): # info Dictionary에 중복된 도시이름이 없다면
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)

# print(info)

# 각 지역별 날씨 텍스트 쓰기
with open('D:\\Django\\workspace\\WebCrawling\\C3_DataProcessing\\forecast.txt', 'wt') as f:
    for loc in sorted(info.keys()): # Dictionary의 Key 값들만 반환해서 List 형식으로 형변환이 일어난다. / sorted는 정렬
        print("+", loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:
            print("-", n)
            f.write('\t'+str(n)+'\n')
