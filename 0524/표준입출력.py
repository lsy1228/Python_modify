print(39)  # 정수형
print("문자열")
print([1,2,3,4,5])  # 리스트형
print(1+2)
print("파" + "이" + "썬")   # 문자열 결합
print("파""이""썬")         # 문자열 결합
print("파","이","썬")       # 콤마는 기본적으로 띄어쓰기가 포함되어 있음
print("파\n\n\n이\n\n썬")
print("\"안녕하세요\"라고 말했습니다")

# end와 sep옵션
print("Hello", end="\n")    # 기본적으로 end 특성에 줄바꿈이 들어가있음
print("파이썬...")

print("Hello", end="@")
print("파이썬...")

print("Hello", end="\t")
print("파이썬...")

print(1,2,3,4,5)
print(1,2,3,4,5, sep="\t")

print("010","5006","4146", sep="-")

year = 2023
month = 5
day = 24
print(year, month, day, sep="/")

# 다양한 출력 스타일
name = "곰돌이"
age = 22
gender = "남자"
job = "소프트웨어 개발자"
addr = "서울특별시 강남구"
# C언어 스타일, %로 서식을 지정하는 형식
print("="*5, "C 스타일", "="*5)
print("이름 : %s" %(name))
print("나이 : %d" %(age))
print("성별 : %s" %(gender))
print("직업 : %s" %(job))
print("주소 : %s" %(addr))
# python 스타일 : 3.6 이전 버전에서 주로 사용
print("="*5, "python old 스타일", "="*5)
print("이름 : {}" .format(name))
print("이름 : {}, 주소 : {}" .format(name, addr))
print("나이 : {}" .format(age))
# python 스타일 : 3.6 이후 스타일
print("="*5, "python new 스타일", "="*5)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"주소 : {addr}")
# JAVA 스타일
print("="*5, "JAVA 스타일", "="*5)
print("이름 : " + name)
print("나이 : " + str(age))
print("성별 : " + gender)

# 출력 포맷 정렬
# < : 좌측 정렬
# > : 우측 정렬
# ^ : 중앙 정렬
print("|{:5}|".format(10))      # 5는 다섯칸을 의미
print("|{:<5}|".format(10))
print("|{:>5}|".format(10))
print("|{:^6}|".format(10))

num = 10
print(f"|{10:5}|")      # 같은 문법
print(f"|{num:5}|")     # 같은 문법
print(f"|{num:<5}|")
print(f"|{num:>5}|")
print(f"|{num:^6}|")

# 소수점 이하 자르기
print(f"{3.141592:.2f}")