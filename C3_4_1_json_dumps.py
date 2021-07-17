import simplejson as json

# Dict(Json) 선언
data = {}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'park',
    'website':'google.com',
    'from':'Busan'
})
data['people'].append({
    'name':'lee',
    'website':'daum.net',
    'from':'Incheon'
})

# Dict(Json) -> Str
e = json.dumps(data, indent=4)
print(type(e))
print(e)

# Str -> Dict(Json)
d = json.loads(e)
print(type(d))
print(d)

with open('D:\Django\workspace\WebCrawling\C3_DataProcessing\member.json', 'w') as f:
    f.write(e)

with open('D:\Django\workspace\WebCrawling\C3_DataProcessing\member.json', 'r') as f:
    r = json.loads(f.read())
    print("============")
    #print(type(r))
    #print(r)
    for p in r['people']:
        print('Name : ' + p['name'])
        print('WebSite : ' + p['website'])
        print('From : ' + p['from'], end='\n\n')
