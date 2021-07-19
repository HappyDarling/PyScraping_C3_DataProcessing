import pandas as pd

# 기본 읽기 1
#df = pd.read_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\excel_s1.xlsx')
df = pd.read_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\excel_s1.xlsx', sheet_name='Sheet1')
# sheet_name 옵션은 엑셀 파일에서 가져올 시트를 정하는데 사용된다.
# 0, 1, 2, 3, ... 넘버링을 사용해서 가져올 수도 있고 정확한 시트의 이름을 지정해서 가져올 수도 있다.
# 옵션을 지정하지 않는다면 디폴트 값으로 0이 지정된다.
print(df) # 전체 시트를 출력한다.
print(df.head(5)) # 전체 시트의 상위 n개를 출력한다. 값을 지정하지 않으면 상위 5개를 출력한다.
print(df.tail(5)) # 전체 시트의 하위 n개를 출력한다. 값을 지정하지 않으면 하위 5개를 출력한다.

# 행, 푸터(Footer, 테일) 스킵
df = pd.read_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\excel_s1.xlsx', skiprows=[0], skip_footer=10)
# 첫 행을 제외하고 아래 행부터 10행을 제외하고 가져온다.
print(df, end='\n\n')

# 헤더 정의 (1)
df = pd.read_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\excel_s1.xlsx', header=0)
print(df)
print(list(df))
print(list(df.columns.values))

# 헤더 정의 (2)
df = pd.read_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\excel_s1.xlsx', skiprows=[0], header=None, names=['State', 2003, 2004, 2005])
print(df, end='\n\n')

# 특정 값 치환
df = pd.read_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\excel_s1.xlsx', header=0, na_values='...', converters={"2003": lambda w: w if w > 60000 else None, "2004": lambda w: w if w < 60000 else None})
# na_values와 converters를 사용해서 특정 조건에 해당하는 값을 원하는 값으로 치환할 수 있다.
# na_values에 '...'를 넣고 converters에 Dictionary 형식으로 입력해준다.
print(df, end='\n\n')
print(pd.isnull(df), end='\n\n') # 위에 converters 조건에 걸린 NaN으로 치환된 값들이 True로 출력되게 된다.

# 실습 정리 및 인덱스 재정의
df = pd.read_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\excel_s1.xlsx', header=0)
print(df.rename(index=lambda x:x+1))
print(df.rename(index=lambda x:x+1).index)
