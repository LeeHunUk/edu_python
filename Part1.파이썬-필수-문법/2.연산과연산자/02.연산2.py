# 1. 비교연산
print(2 > 3) # False
print(15 < 30) # True
print(2 == 3) # False
print(2 != 3) # True
print(2 >= 3) # False
print(3 <= 3) # True
print("=====")

# 2. 논리연산
print(4 < 6 and 10==10) #True and True -> True
print(4 < 6 and 10!=10) #True and False -> False
print(4 < 6 or 10!=10) #True and False -> True
print(not 5==5) # not True -> False
print("=====")

# 3. 멤버십 연산
print("a" in "abc") # 포함 -> True
print("a" in "bcㅇ") # 미포함 -> False
print("a" not in "abc") # 포함 -> False