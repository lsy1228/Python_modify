import pymysql

# 전역 변수
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# MySQL 연결하기
conn = pymysql.connect(host="127.0.0.1", user="root", password="dlthdud", db="mysqlDB", charset="utf8")

# 커서 생성
cur = conn.cursor()

cur.execute("SELECT * FROM userTable")

print("사용자 ID    이름    이메일     출생연도")
print("-"*40)
while True :
    row = cur.fetchone()
    if row == None : break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print(f"{data1:6} {data2:10} {data3:15} {data4:6}")