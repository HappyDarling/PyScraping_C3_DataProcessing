# Sets 자료형 (순서 X, 중복 허용하지 않는다)
# 교집합, 차집합, 합집합 등의 함수를 사용할 때 사용하는 자료형이다. (집합 자료형)

a = set()
b = set([1, 2, 3, 4])

print(type(b))
print(b) # Sets자료형은 이 상태로는 인덱싱이 불가능하다.

t = tuple(b) # Sets자료형을 Tuple형 혹은 List형으로 변환하여 사용해야 한다.
print(type(t), t)
print(t[0:2])

l = list(b)
print(type(l), l)
print(l[0:2])

# 교집합, 합집합, 차집합 함수 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('t - ', s1 & s2) # Sets 자료형에서만 사용할 수 있는 교집합 함수
print('t - ', s1.intersection(s2)) # 교집합 함수

print('t - ', s1 | s2) # 합집합 함수
print('t - ', s1.union(s2))

print('t - ', s1 - s2) # 차집합 함수
print('t - ', s1.difference(s2))

# 추가 제거
s3 = set([0, 1, 2, 3])

s3.add(4)
print('s3 - ', s3)

s3.remove(2)
print('s3 - ', s3)
