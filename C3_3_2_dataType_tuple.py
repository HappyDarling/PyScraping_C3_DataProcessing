# 튜플 자료형(순서 O, 중복 허용, 수정과 삭제는 할 수 없음) : 불변
# 속도 튜플 > 리스트
# 읽기전용 데이터를 사용할때 활용

# 선언
a = ()
b = (0, ) # 원소를 한개만 선언할 경우에는 반드시 뒤에 콤마를 찍어야 한다. 찍지 않는다면 int형으로 저장된다.
c = (0, 0, 1, 2)
d = (0, 1, 'car', 'apple', 'apart')
e = (0, 1, 'car', ('apple', 'apart'))

# 인덱싱
print("#======#")
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0]+d[1]+d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][4])
print('e - ', list(e[-1][1])) # Tuple을 List로 명시적 변환

# 슬라이싱 (리스트와 동일)
print("#======#")
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[3][1][1:3])

# 튜플 연산 (리스트와 동일)
print("#======#")
print('c + d', c+d) # 튜플 + 튜플은 교집합을 제외하지 않고 그대로 합집합해준다.
print('c * 3', c*3) # C 튜플 원소를 3번 중복을 가지는 튜플이 생성된다.
print('hi + c[0]', 'hi' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))