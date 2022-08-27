# 반복문
# : 반복해서 명령을 사용하고 싶을 때

# for문
name = ["김", "이", "박"]

for i in name:
    print(f"나의 성은 {i}씨 입니다.")

# range(시작, 끝+1, 단계)
for i in range(1, 10, 2):
    print(i)

# while
# : 보통 반복 횟수가 정해지지 않았을 때 사용한다.

i = 0
while i < 10: # 조건식
    print(f"{i}번째 반복")

    i += 1 # 증감식

while True:
    x = input("종료하려면 exit를 입력하여 주세요>>")

    if x == "exit":
        break