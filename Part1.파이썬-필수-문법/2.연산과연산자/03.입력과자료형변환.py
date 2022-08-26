# 1. 입력받기
# input("입력할 시 출력할 메세지")

# 2. 자료형 변환
# int(input("입력할 시 출력할 메세지"))

# 실습문제1

x = input("숫자를 입력하세요!")
y = input("다음 숫자를 입력하세요!")

print(x + y) # 문자로 취급

# int 함수로 변환
z = int(input("숫자를 입력하세요!"))
p = int(input("다음 숫자를 입력하세요!"))

print(z + p)

# 실습문제2

year = int(input("태어난 연도를 입력하세요>>>"))

print(f"현재나이는 {2022-year+1}세 입니다.")
