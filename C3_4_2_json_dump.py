import simplejson as json

# Dict(Json) 선언
data = {}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'Seoul',
    'grade':[95, 77, 89, 91]
})
data['people'].append({
    'name':'park',
    'website':'google.com',
    'from':'Busan',
    'grade':[94, 27, 29, 94]
})
data['people'].append({
    'name':'lee',
    'website':'daum.net',
    'from':'Incheon',
    'grade':[45, 74, 81, 50]
})

# json 파일쓰기 (dump)
with open('D:\Django\workspace\WebCrawling\C3_DataProcessing\member.json', 'w') as f:
    json.dump(data, f)

with open('D:\Django\workspace\WebCrawling\C3_DataProcessing\member.json', 'r') as f:
    r = json.load(f)
    print(type(r))
    print(r)
    print("============")
    for p in r['people']:
        print('Name : ' + p['name'])
        print('WebSite : ' + p['website'])
        print('From : ' + p['from'])
        grade = ''
        for g in p['grade']:
            grade = grade + ' ' + str(g)
        print('Grade:', grade.lstrip())
        print(end='\n')
