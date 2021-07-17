# a = 'hello'
# print(type(a))
# print(a[0]) # 리스트로 만들어지지 않았지만 리스트로 자동으로 형변환되서 출력된다
# print(a[0:3])
# print(a[-1:])
#
# for t in a:
#     print(t, end=' ')


# 리스트 자료형(순서 O, 중복 허용, 수정 가능, 삭제 가능)

# 선언
a = []
b = list()
c = [0, 0, 1, 2]
d = [0, 1, 'car', 'apple', 'apart']
e = [0, 1, 'car', ['apple', 'apart']]

# 인덱싱
print("#======#")
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0]+d[1]+d[1])
print('d - ', e[-1][0]) # e[3][0] 으로 해도 같은 결과가 반환된다.

# 슬라이싱
print("#======#")
print('d - ', d[0:3])
print('d - ', d[2:])

# 연산
print("#======#")
print('c + d', c+d) # 리스트 + 리스트는 교집합을 제외하지 않고 그대로 합집합해준다.
print('c * 3', c*3) # C 리스트 원소를 3번 중복을 가지는 리스트가 생성된다.
print('hi + c[0]', 'hi' + str(c[0]))

# 리스트 수정 삭제
print("#======#")
c[0] = 4 # 첫번째 원속의 값을 4로 바꾼다.
print('c - ', c)
c[1] = ['a', 'b', 'c'] # 리스트 안에 리스트를 넣은 것이다.
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # 리스트 안에 리스트를 넣은 것이 아니라 단순히 원소를 수정한 것 이다.
print('c - ', c)
c[1:3] = [] # 리스트의 원소 삭제
print('c - ', c)
del c[3] # c의 3번 인덱스 제거
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]
print("#======#")
print('a - ', a)
a.append(6) # 리스트의 제일 끝에 삽입된다.
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(4), a[4]) # 둘이 값이 동일하다.
print('a - ', a.count(1)) # count 함수는 매개변수로 준 값이 리스트 안에 몇 개가 들어있는지 확인한다.
a.remove(2) # 매개변수의 수를 찾아서 지워버린다.
print('a - ', a)
print('a - ', a.pop()) # Stack과 같이 마지막에 있는 수를 pop시킨다. pop된 수는 리스트에서 사라진다.
print('a - ', a)
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 리스트 삭제 : del, remove, pop

while a: # 리스트를 while에 넣는다면 더이상 리스트에 원소가 없다면 false를 반환하게 된다.
    l = a.pop()
    print(l, end = ' ')
    print(l is 4, end = ' ')
