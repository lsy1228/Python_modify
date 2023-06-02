# 규칙1 : http://naver.com에서 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'n' 개수 + '!' + 자신의 이니셜(예 : 'lsy')

file_name = "password.txt"
f = open(file_name, "wt")
while True : 
    url = input("사이트 : ")
    if(url == "exit") : break
    my_str = url.replace("http://", "")    # http://를 잘라내서 버림
    my_str = my_str[:my_str.index(".")]    # 0번 인덱스부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("n")) + "!" + "lsy"
    f.write(password + "\n")
f.close()