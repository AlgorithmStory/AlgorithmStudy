from sys import stdin

# 입력.
n = int(stdin.readline())
arr = []
for _ in range(n):
    a,b = map(int, stdin.readline().split())
    arr.append([b,a]) # 시작 시간과, 끝나는 시간을 바꿔서 저장. (끝나는 순서를 기준으로 정렬할려고.)

arr.sort()

start_number = arr[0][1]
end_number = arr[0][0]
result_check = 1
# 정렬 이후, 앞에 회의 두번째 부터 탐색.
for i in range(1, n):
    if arr[i][1] >= end_number and arr[i][0] >= end_number: # 현재 가리키는 회의의, 시작시간과 끝나는 시간이, 마지막으로 끝난 회의와 겹치지 않으면, 갱신.
        end_number = arr[i][0]
        start_number = arr[i][1]
        result_check += 1

# 출력.
print(result_check)
