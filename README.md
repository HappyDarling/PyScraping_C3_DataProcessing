데이터의 다양한 형식
XML, JSON, YAML, CSV, ...EXCEL...

HTML : 지정된 태그만 사용할 수 있음 (DIV, P, BR 등)
XML : SGML + HTML, 인터넷에서 쉽게 사용할 수 있고 처리속도가 빠르고 문서작성이 용이해야하고 가독성이 좋고 어려움이 없어야한다.

find와 select의 차이
  CSS선택자나 XPATH를 파싱할때는 Select를 사용했지만
  XML을 파싱할때는 이미 정의된 태그이기 때문에 find 태그 네임으로 사용할 수 있으므로 find가 효율적이다.

pip install simplejson

json.load()는 FILE을 취합니다.
json.load()는 파일(파일 객체)을 예상합니다. 예를 들어 'files/example.json'.

json.loads()는 STRING을 취합니다.
json.loads()는 (유효한) JSON 문자열을 예상합니다. {"foo": "bar"}

Pandas (pip install pandas)
데이터 분석, 데이터 처리를 쉽게 하기 위해 만든 파이썬 패키지
대용량 데이터를 정렬하고 구조화 시켜서 통계, 차트 데이터를 만들어 활용할수 있음

엑셀데이터를 파이썬에서 읽고 쓰기 위해서는 두가지 패키지가 필요하다
pip install xlrd : 읽기
pip install openpyxl : 쓰기
