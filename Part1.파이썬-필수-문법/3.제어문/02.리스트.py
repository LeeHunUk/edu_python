# 1. 리스트 만들기

animals = ["강아지", "고양이", "뱀"]

plus_animals = ["토끼", "사자"]

# 추가
animals.append("말")
print(animals)

# 인덱스 2번에 기린 추가
animals.insert(2, "기린")
print(animals)

# 변경
animals[3] = "코알라"
print(animals)

# 삭제
del animals[4] # 인덱스 삭제
animals.remove("기린") # 데이터 삭제
animals.pop() # 마지막 삭제

print(animals)

# 확장
animals.extend(plus_animals)
print(animals)

# 정렬
animals.sort()
print(animals)

# 뒤집기
animals.reverse()
print(animals)

print(len(animals)) # 길이
print(animals[1:3]) # 슬라이싱
print(animals.index("강아지")) # 위치
print(animals.count("강아지")) # 강아지 개수





