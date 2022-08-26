# 1. 대입연산
# 변수이름 = 데이터


# 2. 산술연산
# - 숫자연산
x = 5
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 몫
print(x % y)  # 나머지
print(x ** y) # 제곱

# - 문자열 연산
t1 = "안녕하세요 "
t2 = "지금은"
t3 = " 파이썬 공부 중입니다."

answer = t1 + t2 + t3
print(answer)

test = answer*3
print(test)

# 복합할당연산자
level = 10
level += 1 # 1 증가

health = 2000
health -= 300 # 300 감소

attack = 300
attack *= 1.5 # 1.5배 증가
print(level, health, attack)

attack /= 1.5 # 1.5배 감소
print(level, health, attack)