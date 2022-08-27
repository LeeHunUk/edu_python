won = input("원화금액을 입력>>")
dollar = input("환율을 입력>>")

try: # 예외가 발생할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError: # 예외가 발생하였을 때 실행
    print("문자열 예외가 발생하였습니다.")
except ZeroDivisionError as e:
    print("나누기 0은 불가능합니다.", e)
else:
   print("예외 발생하지 않은 경우 실행할 코드")
finally:
   print("항상 실행할 코드")