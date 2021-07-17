import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req # 파일을 다운로드 하기 위한 모듈
from bs4 import BeautifulSoup # 내용을 파싱하기 위한 모듈
import os.path
import datetime
from dateutil.relativedelta import relativedelta

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4113563000"
savename = 'D:\Django\\workspace\\WebCrawling\\C3_DataProcessing\\forecast_Yatab.xml'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

todayxml = soup.find('tm').string
today = datetime.datetime.strptime(todayxml, "%Y%m%d%H%M")
data = {} # data / [day, hour, temp, wfKor] 날짜 시간 일기예보
for dt in soup.find_all("data"):
    data[int(dt['seq'])] = []
    data[int(dt['seq'])].append(dt.find("day").string)
    data[int(dt['seq'])].append(dt.find("hour").string)
    data[int(dt['seq'])].append(dt.find("temp").string)
    data[int(dt['seq'])].append(dt.find("wfkor").string)
    #print(data[dt['seq']])

# 일자
# 시 기온 기상정보
# 0 : ['1', '3', '24.0', '맑음'], 202107162300
with open('D:\Django\\workspace\\WebCrawling\\C3_DataProcessing\\forecast_Yatab.txt', 'wt', encoding="utf-8") as f:
    tday = -1
    for dk in sorted(data.keys()):
        if data[dk][0] != tday:
            tday = data[dk][0]
            today = today + relativedelta(days=1)
            print(today.strftime('%Y-%m-%d'))
        print(today.strftime('%H:%M'))
