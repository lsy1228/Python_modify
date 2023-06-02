# 이름 입력
# 나이 입력 : 1 ~ 199까지 입력받고 잘못된 값이 오면 재입력 요청
# 성별 입력 : 영문자 (M과 m은 남성), (F와 f는 여성)으로 입력 받고 나머지는 재입력 요청
# 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재입력 요청
# 결과는 마지막에 한번에 출력

name = input("이름을 입력하세요 : ")

while True :
    age = int(input("나이를 입력하세요 : "))
    if 0 < age < 200 : break
    print("나이를 다시 입력해주세요")
    
while True :
    gender = input("성별을 입력해주세요(M/m or F/f) : ")
    if gender == "M" or gender == "m" :
        gender = "남성"
        break
    elif gender == "F" or gender == "f" :
        gender = "여성"
        break
    else : print("성별을 다시 입력해주세요")

while True :
    job = int(input("직업을 입력해주세요(1.학생 2.회사원 3.주부 4.무직) : "))
    if job == 1 :
        job = "학생"
        break
    elif job == 2 :
        job = "회사원"
        break
    elif job == 3 :
        job = "주부"
        break 
    elif job == 4 :
        job = "무직"
        break
    else :
        print("직업을 다시 선택해주세요")
    
print(f"이름 : {name}, 나이 : {age}, 성별 : {gender}, 직업 : {job}")

# 풀이
name = input("이름을 입력 : ")

while True : 
    age = input("나이 입력 : ")
    if age.isdigit() :     # 입력 받은 문자열이 숫자로 구성되어 있는지 확인
        age = int(age)
        if 0 < age < 200 : break
    print("다시 입력해주세요")

while True :
    gender = input("성별 입력(M/m/F/f) : ")
    if gender == "M" or gender == "m" or gender == "F" or gender == "f" : break
    print("다시 입력해주세요")

while True :
    job = input("직업 입력(1.학생 2.회사원 3.주부 4.무직) : ")
    if job.isdigit() :
        job = int(job)
        if 0 < job < 5 : break
    print("다시 입력해주세요")

if gender == "M" or gender == "m" : gender_prn = "남성"
else : gender_prn = "여성"

job_name = ["", "학생", "회사원", "주부", "무직"]
print("="*5, "회원정보", "="*5)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender_prn}")
print(f"직업 : {job_name[job]}")

