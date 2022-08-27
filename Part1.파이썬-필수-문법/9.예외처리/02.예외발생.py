# raise 구문 사용

try:
    num = int(input("음수를 입력하여 주세요>>"))
    if num >=0:
        raise ValueError("양수는 입력 불가!")
except Exception as e:
    print("에러 발생!", e)