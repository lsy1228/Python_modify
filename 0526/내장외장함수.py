# 내장 함수 : 파이썬 기본적으로 제공하며, import 없이 사용

ls = [1,21,32,43,5,6,7,8,9]
print(sum(ls)/len(ls))      # 평균 구하기

print(sorted(ls))           # 정렬

print(divmod(sum(ls), 5))   # 몫과 나머지

# 외장 함수(import 해서 사용) - 랜덤
import random

# 지정한 범위 내의 임의의 수 구하는 함수
rand = random.randint(0, 4)     # 0 ~ 4 사이의 임의의 값 생성(미만 개념 X)
print(rand)

rand = random.randrange(0, 4)   # 0 ~ 4 미만의 임의의 값 생성(미만 개념 O)
print(rand)

# 현재 시간 가져오기 
from datetime import datetime     # datetime 내부에서 datetime함수를 가져 옴

datetime.today()                  # 현재 날짜 가져오기
datetime.today().year             # 현재 연도 가져오기
datetime.today().month            # 현재 월 가져오기
datetime.today().day              # 현재 일 가져오기
datetime.today().hour             # 현재 시간 가져오기

print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 중복 값이 없는 로또 번호 생성
import random
print("로또 번호 자동 생성 : ", end="")
ls = []
while True :
    rand = random.randrange(1,46)
    if rand not in ls :
        ls.append(rand)
    if len(ls) == 6 : break
print(ls)
