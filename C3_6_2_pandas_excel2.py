import pandas as pd

df = pd.read_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\excel_s1.xlsx')
print(df, end='\n\n')

# 컬럼 값 수정
df['State'] = df['State'].str.replace(' ', '|')
print(df, end='\n\n')

# 평균 컬럼 추가
df['Avg'] = df[['2003', '2004', '2005']].mean(axis=1).round(2) # 1은 가로 평균, 0은 세로 평균 / round는 반올림
print(df, end='\n\n')

# 합계 컬럼 추가
df['Avg'] = df[['2003', '2004', '2005']].sum(axis=1) # 1은 가로 합계, 0은 세로 합계
print(df, end='\n\n')

# 최대값 출력
print(df[['2003', '2004', '2005']].max(axis=0), end='\n\n')

# 최소값 출력
print(df[['2003', '2004', '2005']].min(axis=0), end='\n\n')

# 상세 정보 출력
print(df.describe(), end='\n\n') # count, mean, std, min, 25%, 50%, 75%, max

# 저장
df.to_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\results_s1.xlsx', index=None)
