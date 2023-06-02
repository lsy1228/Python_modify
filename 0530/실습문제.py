# 입력 받은 수가 소수인지 아닌지 판별하기 (함수 이용)
# 소수 : 1과 자기자신 이외의 수로 나누어지지 않는 수

def prime(num) :
    for i in range(2, num) :
        if num % i == 0 : return False
    return True

num = int(input("수 입력 : "))
if prime(num) : print(f"{num}은 소수 입니다")
else : print(f"{num}은 소수가 아닙니다")