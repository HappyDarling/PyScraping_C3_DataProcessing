import pandas as pd

# 기본 읽기
df = pd.read_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\csv_s1.csv')
print(df, end='\n\n') # 맨 위의 라인은 헤더로 표현, 각 라인에 인덱스 콜론을 붙여준다.

# 행 스킵
df = pd.read_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\csv_s1.csv', skiprows=[0, 1])
# 첫 번째 라인과 두 번째 라인을 생략. 세번째 라인이 헤더가 된다.
print(df, end='\n\n')

# 행 스킵, 헤더 생략
df = pd.read_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\csv_s1.csv', skiprows=[0], header=3)
# 헤더를 지정해줄 수 있다. 정수를 매개로 받으며 매개로 받은 곳부터 시작한다. None을 지정하면 0 1 2 3으로 헤더가 된다.
print(df, end='\n\n')

# 헤더 정의
df = pd.read_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015])
# 첫번째 줄을 생략하고, 헤더가 자동으로 생성되는 것을 막고, 헤더를 지정한 문자열으로 설정한다.
print(df, end='\n\n')

# 인덱스 컬럼 정의
df = pd.read_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015], index_col=[0])
# 인덱스를 구성하는 칼럼을 임의로 지정한다.
print(df, end='\n\n')

# na_values 특정값 치환
df = pd.read_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015], index_col=[0], na_values=['JAN'])
# 리스트 안에 해당하는 것들을 NaN으로 변환해준다. 이는 isnull 함수를 통해서 True False를 알아낼 수 있다.
print(pd.isnull(df), end='\n\n')

# 실습 정리 및 인덱스 재정의
df = pd.read_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015])
# 리스트 안에 해당하는 것들을 NaN으로 변환해준다. 이는 isnull 함수를 통해서 True False를 알아낼 수 있다.
print(df.index, end='\n\n') # 인덱스의 타입 형식과 인덱스 요소를 출력
print(list(df.index), end='\n\n') # 인덱스 리스트 1
print(df.index.values, end='\n\n') # 인덱스를 출력은 하지만 리스트는 아니다.
print(df.index.values.tolist(), end='\n\n') # 인덱스 리스트 2

print(df.rename(index={0:'aa', 1:'bb', 2:'cc'}), end='\n\n') # 인덱스 재정의
print(df.rename(index=lambda x:x*10), end='\n\n') # 인덱스 재정의 (람다식)

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
