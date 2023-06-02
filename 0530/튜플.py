# 튜플 : 변경할 수 없는 시퀀스 자료형, () 괄호를 사용하여 생성
# 패킹과 언패킹 개념이 있음
# 튜플 정의하기
person = "곰돌이", 25, "서울"      # () 괄호를 생략해도 튜플, 쓰기 불가 특성

# 튜플 언팩킹 : 구조 분해랑 유사
name, age, city = person
print(name)
print(age)
print(city) 

# 튜플을 이용한 함수 반환값 다루기
def get_person() :
    name = "곰돌이"
    age = 22
    city = "서울"
    return name, age, city      # return 값을 여러개 넘길 수 있음
result = get_person()     # 튜플의 패킹 동작
print(result)             

a,b,c = get_person()
print(a,b,c)

# 기본적인 동작 
tp = 1,2,3,4,5,6,7,8,9,10,1,1,2,2,3,3
print(tp.count(3))      # 원하는 데이터의 개수를 세어주는 함수 (리스트와 동일)
print(tp.index(3))      # 원하는 데이터의 시작 인덱스를 알려줌
print(len(tp))          # 튜플에 포함된 데이터의 개수
print(tp.__len__())     # 튜플에 포함된 데이터의 개수

# 튜플에서 사용이 안되는 것 : 삭제 안됨
t1 = 1,2,3,4,5
del t1[0]