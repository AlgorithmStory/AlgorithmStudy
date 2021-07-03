from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))
arr.sort() # 입력 받자마자 정렬.

if n%2==0: # 입력 횟수가 짝수면, 가운데에서 왼쪽 값 출력.
    print(arr[int(n/2)-1])
else: # 홀수면 정 가운데 출력.
    print(arr[int(n/2)])
