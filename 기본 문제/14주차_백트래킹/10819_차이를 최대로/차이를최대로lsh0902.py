from itertools import permutations
T = int(input())
nums = list(map(int, input().split()))
permu = permutations(nums, T)
biggest = 0
for num in permu:
    res = 0
    for i in range(len(num)-1):
        res += max(abs(num[i] - num[i+1]), abs(num[i+1] - num[i]))
    biggest = res if res > biggest else biggest
print(biggest)
