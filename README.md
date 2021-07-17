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
