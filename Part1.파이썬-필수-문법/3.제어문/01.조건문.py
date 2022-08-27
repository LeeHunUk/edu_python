# 조건문
# : 조건에 따라 실행할 명령이 달라 지는 것

origin_pass = "1234"
input_pass = input("패스를 입력하세요>>")

if input_pass == origin_pass:
    print("성공")
elif input_pass=="":
    print("비어있습니다.")
else:
    print("실패")