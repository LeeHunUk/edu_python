# 리스트 내포
# for 사용
nums = [i for i in range(5)]
print(nums)

nums2 = [100, 220, 300]
double = [i * 2 for i in nums2]
print(double)

nums3 = [i for i in range(10) if i % 2 == 0]
print(nums3)