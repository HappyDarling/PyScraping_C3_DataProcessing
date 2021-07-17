# 딕셔너리 자료형
# Json Data와 비슷하며 Key와 Value가 한 쌍으로 이루어진 자료형이다.
# 순서가 존재하지 않고 중복을 허용하지 않는다. 수정과 삭제는 가능하다.
# 매번 실행할 때 마다 순서가 섞여서 출력된다.

# 선언
a = {'name' : 'kim', 'phone' : '01077777777', 'birth' : 910809}
b = {0 : 'Hello World!'} # Key 값은 정수형으로도 선언할 수 있다.
c = {'arr' : [0, 1, 2, 3]} # List 배열을 Value값으로 넣을 수 있다.
print(type(a), a)

# 출력
print('a - ', a['name'])
print('a - ', a.get('name'))

# print('a - ', a['address']) # 없는 키 값으로 가져오려고 한다면 예외가 발생한다.
print('a - ', a.get('address')) # get으로 가져오려고 하면 예외가 발생하지 않고 None이 반환된다.

print('c - ', type(c.get('arr')))

# 딕셔너리 추가
a['address'] = 'Seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

print('a - ', list(a.keys()))
print('a - ', a.keys())

print('a - ', list(a.values()))
print('a - ', a.values())

print('a - ', a.items()) # Key와 Value를 묶어서 Tuple로 반환해주는 함수이다.
print('a - ', type(list(a.items())[1]))

print('a - ', 'name' in a) # True
print('a - ', 'city' in a) # False
