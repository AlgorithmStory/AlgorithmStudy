import sys
from sys import stdin
sys.setrecursionlimit(50000)

def recursion(nums):
    length = len(nums)

    # 요소가 1개면 리턴.
    if length <= 1:
        return nums

    # 길이 만큼 도는데,
    for i in range(1, length):

        # 첫번째 원소보다 큰게 발견되면,
        if nums[i] > nums[0]:

            # 첫번째 원소를 젤 마지막으로 보내고, 인덱싱 잘 해서 재귀 리턴 함.
            return recursion(nums[1:i]) + recursion(nums[i:]) + [nums[0]]

    return recursion(nums[1:]) + [nums[0]]


# 따로 정해진 입력의 횟수가 없어서, 예외처리로 받음.
nums = []
while True:
    try:
        nums.append(int(stdin.readline()))
    except:
        break

# 함수 실행.
nums = recursion(nums)

# 출력.
for n in nums:
    print(n)
