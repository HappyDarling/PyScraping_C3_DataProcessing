import pandas as pd
import numpy as np

# 랜덤으로 DataFrame 생성
df = pd.DataFrame(np.random.randint(0, 100, size=(100,4)), columns=list('ABCD')) # ['A', 'B', 'C', 'D'] 와 동일하다.
# 0부터 100까지의 수를 랜덤하게 4개의 열, 100개의 행으로 이루어지게 DataFrame을 생성.
# 칼럼의 이름은 ABCD
print(df)

df = pd.DataFrame(np.random.randn(100,4), columns=list('ABCD'))
print(df)

df.to_excel('D:\Django\workspace\WebCrawling\C3_DataProcessing\\result_xlsx.xlsx', index=False)
#df.to_csv('D:\Django\workspace\WebCrawling\C3_DataProcessing\\result_csv.xlsx', index=False, header=False)
