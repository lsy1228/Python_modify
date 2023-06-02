# 집합은 주로 다른 자료형의 중복 제거 할 때 자주 사용
# 순서가 없음, 중복 불가, mutable(읽기/쓰기) 특성

# 중복 제거
s1 = set([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
print(s1)

s2 = set([1,2,3,4,5])
s3 = set([1,3,7,6,8,9])
# 교집합 : 양쪽에 모두 존재하는 요소만 선택
print(s2.intersection(s3))

# 합집합
print(s2.union(s3))

# 차집합
print(s2.difference(s3))

# 중복 제거로 로또 번호 만들기
import random
lotto = set()
while True :        
    num = random.randrange(1, 46)
    lotto.add(num)
    if len(lotto) == 6 : break
print(lotto)