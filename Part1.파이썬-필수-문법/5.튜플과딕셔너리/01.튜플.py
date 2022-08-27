# 튜플의 특징
'''
1. 시퀀스 자료형
2. 수정, 추가, 삭제가 불가능한 리스트
3. 메모리 사용이 효율적
4. 읽기만 가능하기 때문에 데이터 손실의 염려가 없다.
튜플 = (데이터, 데이터, 데이터)
튜플 = 데이터, 데이터, 데이터
'''

# 튜플 만들기
x = list(range(10))

a = tuple(x)
b = list(a)

# 패킹
numbers = 3, 4, 5

# 언패킹
c, d, e = numbers

# 튜플 함수
print(a.index(0))  # 인덱스 구하기

print(a.count(3))  # 값 개수

print(max(a), min(a))  # 최대, 최소

print(sum(a))  # 합계