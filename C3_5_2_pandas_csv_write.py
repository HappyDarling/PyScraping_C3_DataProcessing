import pandas as pd

# 읽기 (구분자 Separator가 다른 문자로 되어있는 경우)
df2 = pd.read_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\csv_s2.csv', sep=';', skiprows=[0], header=None, names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
print(df2, end='\n\n')

# 컬럼 이름을 가지고 그 컬럼의 요소만 출력이 가능하다
print(df2['Grade'])

# 컬럼의 내용을 쉽게 수정할 수 있음
df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
print(df2['Grade'])

# Avg 평균 컬럼 추가
df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1)
print(df2)

# Sum 합계 컬럼 추가
df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
print(df2)

#df2.to_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\result_csv.csv') # 인덱스까지 파일에 작성한다. 인덱스가 없는 열은 공란으로 남는다.
df2.to_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\result_csv.csv', index=False) # 인덱스를 제거하고 파일에 작성한다.
