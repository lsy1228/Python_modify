# 입력 받은 n개의 원소에 대한 평균 구하기
value = list(map(int, input("정수 입력 : ").split()))
print(sum(value)/len(value))

# 정수 n을 입력 받아 n * n 출력하기
n = int(input("정수 입력 : "))
for i in range(1, n*n+1) :
    print(f"{i:4}", end="")
    if(i % n == 0) : print()

# n개에 대한 숫자를 입력 받아 최소값 및 최대값 구하기
n = list(map(int, input().split()))
print(min(n))
print(max(n))

# 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
from datetime import datetime

current_year = datetime.today().year    # 현재가 몇년인지 확인
jumin = input("주민등록번호 : ")
jumin_year = int(jumin[:2])
jumin_gender = int(jumin[6])
jumin_month = int(jumin[2:4])
jumin_day = int(jumin[4:6])

if jumin_gender == 1 or jumin_gender == 2 :
    age = current_year - 1900 - jumin_year
else :
    age = current_year - 2000 - jumin_year

if jumin_gender == 1 or jumin_gender == 3 :
    gender = "남성"
else :
    gender = "여성"
print(f"당신은  {jumin_year}년 {jumin_month}월 {jumin_day}일 생입니다")
print(f"당신의 성별은 {gender}입니다")
print(f"당신의 나이는 {age}입니다")


