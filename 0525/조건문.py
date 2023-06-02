# 조건문 : if ~ else
num = int(input("정수 입력하세요 : "))
if num % 2 == 0 :
    print("짝수 입니다")
else :
    print("홀수 입니다")

# 조건문 : if ~ elif ~ else
n = int(input("정수 입력하세요 : "))
if n > 100 :
    print("100보다 커요")
elif n < 100 :
    print("100보다 작아요")
else :
    print("100과 같아요")

print("지금 계절은? : ", end='');
season = input()
if season == "spring": print("봄이 왔어요.")
elif season == "summer": print("여름이 왔어요.")
elif season == "fall" or season == "autumn" : print("쓸쓸한 가을 입니다.")
elif season == "winter": print("아직 겨울이네요ㅠㅠ")
else : pass

age = int(input("나이를 입력하세요 : "))
if(0 < age < 200) :
    print("정상 입력 입니다")
else :
    print("잘못 입력하셨습니다")

# 회원가입을 위한 아이디와 패스워드 입력받기
# string.find(찾을 문자)
# string.find(찾을 문자, 시작 index)
# string.find(찾을 문자, 시작 index, 끝 index)
user = input("아이디 입력 : ")
if len(user) >= 10 :
    pw = input("비밀번호 입력 : ")
    if pw.__len__() < 8 or pw.__len__() > 16 :
        print("비밀번호는 8자리에서 16자리 사이어야 합니다")
    else :
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")
else :
    print("아이디는 반드시 10자리 이상이어야 합니다")