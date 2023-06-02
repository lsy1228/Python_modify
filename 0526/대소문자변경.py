# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력

result = ""
for e in input() :
    if e.islower() :
        result += e.upper()
    else :
        result += e.lower()
print(result)

# 3개의 자연수 입력받아 모두 곱함
# 결과값에서 나오는 숫자의 횟수를 출력
# 17037300 => 0은 3번, 1은 1번, 7은 2번

a, b, c = map(int, input("정수 3개 입력 : ").split())
ls = list(str(a * b * c))
for i in range(10) :
    print(ls.count(str(i)))     # 해당 문자의 개수 반환
