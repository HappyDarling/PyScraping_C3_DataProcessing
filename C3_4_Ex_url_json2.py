import urllib.request as req
import simplejson as json
import os.path

url = 'https://jsonplaceholder.typicode.com/comments'
savename = 'D:\Django\workspace\WebCrawling\C3_DataProcessing\\comments.json'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

r = json.load(open(savename, 'r', encoding="utf-8"))

for i in r:
    print(i['email'])
    print(i['body'], end='\n=========\n')
